import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from tkinter.scrolledtext import ScrolledText
import threading
from datetime import datetime
from scraper import GazaScraper
import webbrowser

class GazaNewsGUI:
    def __init__(self, root):
        self.root = root
        self.scraper = GazaScraper()
        self.language = "en"
        self.current_news = []
        
        self.root.title("Gaza News Portal")
        self.root.geometry("900x700")
        self.root.configure(bg='#f0f2f5')
        
        self.setup_styles()
        
        self.create_widgets()
        
        self.update_language()
    
    def setup_styles(self):
        style = ttk.Style()
        style.theme_use('clam')
        
        style.configure('Header.TLabel', 
                       font=('Arial', 18, 'bold'),
                       background='#f0f2f5',
                       foreground='#2c3e50')
        
        style.configure('Action.TButton',
                       font=('Arial', 10, 'bold'),
                       padding=(20, 10))
        
        style.configure('Language.TButton',
                       font=('Arial', 9),
                       padding=(10, 5))
        
        style.configure('Custom.Treeview',
                       background='white',
                       foreground='#2c3e50',
                       fieldbackground='white',
                       font=('Arial', 9))
        
        style.configure('Custom.Treeview.Heading',
                       font=('Arial', 10, 'bold'),
                       background='#3498db',
                       foreground='white')
    
    def create_widgets(self):
        header_frame = tk.Frame(self.root, bg='#3498db', height=80)
        header_frame.pack(fill='x', pady=(0, 20))
        header_frame.pack_propagate(False)
        
        title_frame = tk.Frame(header_frame, bg='#3498db')
        title_frame.pack(expand=True, fill='both')
        
        self.title_label = tk.Label(title_frame, 
                                   text="Gaza News Portal",
                                   font=('Arial', 20, 'bold'),
                                   bg='#3498db',
                                   fg='white')
        self.title_label.pack(side='left', padx=20, pady=20)
        
        self.language_btn = ttk.Button(title_frame,
                                      text="العربية",
                                      style='Language.TButton',
                                      command=self.toggle_language)
        self.language_btn.pack(side='right', padx=20, pady=20)
        
        main_frame = tk.Frame(self.root, bg='#f0f2f5')
        main_frame.pack(fill='both', expand=True, padx=20)
        
        left_panel = tk.LabelFrame(main_frame, 
                                  text="Controls",
                                  font=('Arial', 12, 'bold'),
                                  bg='#f0f2f5',
                                  fg='#2c3e50',
                                  padx=10, pady=10)
        left_panel.pack(side='left', fill='y', padx=(0, 10))
        
        self.latest_news_btn = ttk.Button(left_panel,
                                         text="View Latest News",
                                         style='Action.TButton',
                                         command=self.load_latest_news)
        self.latest_news_btn.pack(fill='x', pady=5)
        
        search_frame = tk.Frame(left_panel, bg='#f0f2f5')
        search_frame.pack(fill='x', pady=10)
        
        self.search_label = tk.Label(search_frame,
                                    text="Search Keyword:",
                                    font=('Arial', 10),
                                    bg='#f0f2f5',
                                    fg='#2c3e50')
        self.search_label.pack(anchor='w')
        
        self.search_entry = tk.Entry(search_frame,
                                    font=('Arial', 10),
                                    relief='solid',
                                    bd=1)
        self.search_entry.pack(fill='x', pady=(5, 0))
        
        self.search_btn = ttk.Button(search_frame,
                                    text="Search",
                                    command=self.search_news)
        self.search_btn.pack(fill='x', pady=5)
        
        date_frame = tk.Frame(left_panel, bg='#f0f2f5')
        date_frame.pack(fill='x', pady=10)
        
        self.date_label = tk.Label(date_frame,
                                  text="Filter by Date:",
                                  font=('Arial', 10),
                                  bg='#f0f2f5',
                                  fg='#2c3e50')
        self.date_label.pack(anchor='w')
        
        self.date_entry = tk.Entry(date_frame,
                                  font=('Arial', 10),
                                  relief='solid',
                                  bd=1)
        self.date_entry.pack(fill='x', pady=(5, 0))
        self.date_entry.insert(0, "DD/MM/YYYY")
        
        self.filter_btn = ttk.Button(date_frame,
                                    text="Filter",
                                    command=self.filter_by_date)
        self.filter_btn.pack(fill='x', pady=5)
        
        self.save_btn = ttk.Button(left_panel,
                                  text="Save to CSV",
                                  command=self.save_to_csv)
        self.save_btn.pack(fill='x', pady=5)
        
        right_panel = tk.LabelFrame(main_frame,
                                   text="News Articles",
                                   font=('Arial', 12, 'bold'),
                                   bg='#f0f2f5',
                                   fg='#2c3e50',
                                   padx=10, pady=10)
        right_panel.pack(side='right', fill='both', expand=True)
        
        tree_frame = tk.Frame(right_panel, bg='#f0f2f5')
        tree_frame.pack(fill='both', expand=True)
        
        self.tree = ttk.Treeview(tree_frame,
                                style='Custom.Treeview',
                                columns=('Date', 'Title'),
                                show='headings',
                                height=20)
        
        self.tree.heading('Date', text='Date')
        self.tree.heading('Title', text='Title')
        self.tree.column('Date', width=100, minwidth=80)
        self.tree.column('Title', width=400, minwidth=200)
        
        v_scrollbar = ttk.Scrollbar(tree_frame, orient='vertical', command=self.tree.yview)
        h_scrollbar = ttk.Scrollbar(tree_frame, orient='horizontal', command=self.tree.xview)
        self.tree.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)
        
        self.tree.pack(side='left', fill='both', expand=True)
        v_scrollbar.pack(side='right', fill='y')
        h_scrollbar.pack(side='bottom', fill='x')
        
        self.tree.bind('<Double-1>', self.open_article)
        
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        status_bar = tk.Label(self.root,
                             textvariable=self.status_var,
                             relief='sunken',
                             anchor='w',
                             bg='#ecf0f1',
                             fg='#2c3e50')
        status_bar.pack(side='bottom', fill='x')
        
        self.progress = ttk.Progressbar(self.root,
                                       mode='indeterminate')
        self.progress.pack(side='bottom', fill='x')
    
    def toggle_language(self):
        if self.language == "en":
            self.language = "ar"
        else:
            self.language = "en"
        self.update_language()
    
    def update_language(self):
        if self.language == "en":
            texts = {
                'title': "Gaza News Portal",
                'language_btn': "العربية",
                'controls': "Controls",
                'latest_news': "View Latest News",
                'search_label': "Search Keyword:",
                'search_btn': "Search",
                'date_label': "Filter by Date:",
                'filter_btn': "Filter",
                'save_btn': "Save to CSV",
                'news_articles': "News Articles",
                'date_col': "Date",
                'title_col': "Title",
                'ready': "Ready"
            }
        else:
            texts = {
                'title': "بوابة أخبار غزة",
                'language_btn': "English",
                'controls': "أدوات التحكم",
                'latest_news': "عرض آخر الأخبار",
                'search_label': "البحث بالكلمة المفتاحية:",
                'search_btn': "بحث",
                'date_label': "تصفية حسب التاريخ:",
                'filter_btn': "تصفية",
                'save_btn': "حفظ في ملف CSV",
                'news_articles': "المقالات الإخبارية",
                'date_col': "التاريخ",
                'title_col': "العنوان",
                'ready': "جاهز"
            }
        
        self.title_label.config(text=texts['title'])
        self.language_btn.config(text=texts['language_btn'])
        self.latest_news_btn.config(text=texts['latest_news'])
        self.search_label.config(text=texts['search_label'])
        self.search_btn.config(text=texts['search_btn'])
        self.date_label.config(text=texts['date_label'])
        self.filter_btn.config(text=texts['filter_btn'])
        self.save_btn.config(text=texts['save_btn'])
        
        self.tree.heading('Date', text=texts['date_col'])
        self.tree.heading('Title', text=texts['title_col'])
        
        self.status_var.set(texts['ready'])
    
    def show_loading(self):
        self.progress.start(10)
    
    def hide_loading(self):
        self.progress.stop()
    
    def update_status(self, message):
        self.status_var.set(message)
        self.root.update_idletasks()
    
    def populate_tree(self, news_data):
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for news in news_data:
            date_str = news['date'].strftime('%d/%m/%Y') if news['date'] else 'N/A'
            self.tree.insert('', 'end', values=(date_str, news['title']))
    
    def load_latest_news(self):
        def load_news():
            try:
                self.show_loading()
                self.update_status("Loading latest news..." if self.language == "en" else "جاري تحميل آخر الأخبار...")
                
                news = self.scraper.get_latest_news()
                self.current_news = news
                
                self.root.after(0, lambda: self.populate_tree(news))
                self.root.after(0, lambda: self.update_status(f"Loaded {len(news)} articles" if self.language == "en" else f"تم تحميل {len(news)} مقال"))
                
            except Exception as e:
                self.root.after(0, lambda: messagebox.showerror("Error", f"Failed to load news: {str(e)}"))
                self.root.after(0, lambda: self.update_status("Error loading news" if self.language == "en" else "خطأ في تحميل الأخبار"))
            finally:
                self.root.after(0, self.hide_loading)
        
        thread = threading.Thread(target=load_news)
        thread.daemon = True
        thread.start()
    
    def search_news(self):
        keyword = self.search_entry.get().strip()
        if not keyword:
            messagebox.showwarning("Warning", "Please enter a keyword" if self.language == "en" else "يرجى إدخال كلمة مفتاحية")
            return
        
        def search():
            try:
                self.show_loading()
                self.update_status("Searching..." if self.language == "en" else "جاري البحث...")
                
                news = self.scraper.search_key(keyword)
                self.current_news = news
                
                self.root.after(0, lambda: self.populate_tree(news))
                self.root.after(0, lambda: self.update_status(f"Found {len(news)} articles for '{keyword}'" if self.language == "en" else f"تم العثور على {len(news)} مقال لـ '{keyword}'"))
                
            except Exception as e:
                self.root.after(0, lambda: messagebox.showerror("Error", f"Search failed: {str(e)}"))
                self.root.after(0, lambda: self.update_status("Search error" if self.language == "en" else "خطأ في البحث"))
            finally:
                self.root.after(0, self.hide_loading)
        
        thread = threading.Thread(target=search)
        thread.daemon = True
        thread.start()
    
    def filter_by_date(self):
        date_str = self.date_entry.get().strip()
        if date_str == "DD/MM/YYYY" or not date_str:
            messagebox.showwarning("Warning", "Please enter a valid date" if self.language == "en" else "يرجى إدخال تاريخ صحيح")
            return
        
        try:
            target_date = datetime.strptime(date_str, "%d/%m/%Y").date()
        except ValueError:
            messagebox.showerror("Error", "Invalid date format. Use DD/MM/YYYY" if self.language == "en" else "تنسيق تاريخ غير صحيح. استخدم DD/MM/YYYY")
            return
        
        def filter_news():
            try:
                self.show_loading()
                self.update_status("Filtering by date..." if self.language == "en" else "جاري التصفية حسب التاريخ...")
                
                news = self.scraper.filter_date(target_date)
                self.current_news = news
                
                self.root.after(0, lambda: self.populate_tree(news))
                self.root.after(0, lambda: self.update_status(f"Found {len(news)} articles for {date_str}" if self.language == "en" else f"تم العثور على {len(news)} مقال لتاريخ {date_str}"))
                
            except Exception as e:
                self.root.after(0, lambda: messagebox.showerror("Error", f"Filter failed: {str(e)}"))
                self.root.after(0, lambda: self.update_status("Filter error" if self.language == "en" else "خطأ في التصفية"))
            finally:
                self.root.after(0, self.hide_loading)
        
        thread = threading.Thread(target=filter_news)
        thread.daemon = True
        thread.start()
    
    def save_to_csv(self):
        if not self.current_news:
            messagebox.showwarning("Warning", "No data to save" if self.language == "en" else "لا توجد بيانات للحفظ")
            return
        
        try:
            filename = filedialog.asksaveasfilename(
                defaultextension=".csv",
                filetypes=[("CSV files", "*.csv"), ("All files", "*.*")],
                title="Save news to CSV" if self.language == "en" else "حفظ الأخبار في ملف CSV"
            )
            
            if filename:
                self.scraper.save_to_csv(self.current_news)
                import shutil
                shutil.move("GazaNews.csv", filename)
                messagebox.showinfo("Success", f"News saved to {filename}" if self.language == "en" else f"تم حفظ الأخبار في {filename}")
                self.update_status("Data saved successfully" if self.language == "en" else "تم حفظ البيانات بنجاح")
        
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save: {str(e)}")
            self.update_status("Save error" if self.language == "en" else "خطأ في الحفظ")
    
    def open_article(self, event):
        selection = self.tree.selection()
        if not selection:
            return
        
        item = self.tree.item(selection[0])
        title = item['values'][1]
        
        for news in self.current_news:
            if news['title'] == title and news['link']:
                webbrowser.open(news['link'])
                break

def main():
    root = tk.Tk()
    app = GazaNewsGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()