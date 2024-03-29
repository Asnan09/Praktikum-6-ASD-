YELLOW = "\033[93m"
RESET = "\033[0m"
PINK = "\033[95m"
BLUE = "\033[94m"

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Stack is empty")
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Stack is empty")
            return None

    def size(self):
        return len(self.items)
    
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("Queue is empty")
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            print("Queue is empty")
            return None

    def size(self):
        return len(self.items)

class Barang:
    def __init__(self, id_barang, nama, harga, stok, kategori):
        self.id_barang = id_barang
        self.nama = nama
        self.harga = harga
        self.stok = stok
        self.kategori = kategori
        self.next = None

class TokoBangunan:
    def __init__(self):
        self.head = None
        self.stack = Stack()
        self.queue = Queue()

    def fibonacci_search(self, attribute, value):
        if attribute == 'id_barang':
            comparison_key = lambda x: x.id_barang
        elif attribute == 'nama':
            comparison_key = lambda x: x.nama
        else:
            print("Attribute not supported for searching.")
            return None

        def fibonacci(n):
            if n <= 0:
                return 0
            elif n == 1:
                return 1
            else:
                return fibonacci(n - 1) + fibonacci(n - 2)

        def fibonacci_search_util(items, value):
            n = len(items)
            offset = -1
            fib_m_minus_2 = 0
            fib_m_minus_1 = 1
            fib = fib_m_minus_1 + fib_m_minus_2

            while fib < n:
                fib_m_minus_2 = fib_m_minus_1
                fib_m_minus_1 = fib
                fib = fib_m_minus_1 + fib_m_minus_2

            while fib > 1:
                i = min(offset + fib_m_minus_2, n - 1)

                if comparison_key(items[i]) < value:
                    fib = fib_m_minus_1
                    fib_m_minus_1 = fib_m_minus_2
                    fib_m_minus_2 = fib - fib_m_minus_1
                    offset = i
                elif comparison_key(items[i]) > value:
                    fib = fib_m_minus_2
                    fib_m_minus_1 = fib_m_minus_1 - fib_m_minus_2
                    fib_m_minus_2 = fib - fib_m_minus_1
                else:
                    return i

            if fib_m_minus_1 and offset < n - 1 and comparison_key(items[offset + 1]) == value:
                return offset + 1

            return None

        items = []
        current = self.head
        while current:
            items.append(current)
            current = current.next

        idx = fibonacci_search_util(items, value)
        if idx is not None:
            return items[idx]
        else:
            print("Barang tidak ditemukan.")
            return None

    def search_by_id(self, id_barang):
        return self.fibonacci_search('id_barang', id_barang)

    def search_by_name(self, nama_barang):
        return self.fibonacci_search('nama', nama_barang)


    def tambah_barang_di_awal(self, barang):
        barang.next = self.head
        self.head = barang

    def tambah_barang_di_akhir(self, barang):
        if not self.head:
            self.head = barang
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = barang

    def tampilkan_stack(self):
        print("Isi Stack:")
        current = self.head
        while current:
            self.stack.push(current)
            print(current.id_barang, end=" ")
            current = current.next  
        print()
        print("Elemen teratas:", self.stack.peek().id_barang if not self.stack.is_empty() else "Stack kosong")
        print("Size Stack:", self.stack.size())

    def tampilkan_queue(self): 
        print("Isi Queue:")
        current = self.head
        while current:
            self.queue.enqueue(current)
            print(current.id_barang, end=" ")
            current = current.next
        print()
        print("Elemen di depan antrian:", self.queue.peek().id_barang if not self.queue.is_empty() else "Queue kosong")
        print("Ukuran Antrian:", self.queue.size())

    def tambah_barang_di_antara(self, barang, id_sebelumnya):
        if not self.head:
            print("Linked list kosong.")
            return
        current = self.head
        while current:
            if current.id_barang == id_sebelumnya:
                barang.next = current.next
                current.next = barang
                return
            current = current.next
        print(f"Tidak ditemukan barang dengan ID {id_sebelumnya}. Barang tidak ditambahkan.")

    def hapus_barang_di_awal(self):
        if not self.head:
            print("Linked list kosong.")
            return
        self.head = self.head.next

    def hapus_barang_di_akhir(self):
        if not self.head:
            print("Linked list kosong.")
            return
        if not self.head.next:
            self.head = None
            return
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    def hapus_barang_di_antara(self, id_sebelumnya):
        if not self.head:
            print("Linked list kosong.")
            return
        if self.head.id_barang == id_sebelumnya:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.id_barang == id_sebelumnya:
                current.next = current.next.next
                return
            current = current.next
        print(f"Tidak ditemukan barang dengan ID {id_sebelumnya}. Barang tidak dihapus.")

    def tampilkan_barang(self):
        current = self.head
        while current:
            print(f"ID: {current.id_barang}, Nama: {current.nama}, Harga: {current.harga}, Stok: {current.stok}, Kategori: {current.kategori}")
            current = current.next

    def quick_sort(self, attribute, order='ascending'):
        items = []
        current = self.head
        while current:
            items.append(current)
            current = current.next
        if attribute == 'id_barang':
            comparison_key = lambda x: x.id_barang
        elif attribute == 'nama':
            comparison_key = lambda x: x.nama
        else:
            print("Attribute not supported for sorting.")
            return
        
        reverse = order.lower() == 'descending'

        def partition(low, high):
            pivot = items[high]
            i = low - 1
            for j in range(low, high):
                if (comparison_key(items[j]) < comparison_key(pivot)) ^ reverse:
                    i += 1
                    items[i], items[j] = items[j], items[i]
            items[i + 1], items[high] = items[high], items[i + 1]
            return i + 1

        def quick_sort_util(low, high):
            if low < high:
                pi = partition(low, high)
                quick_sort_util(low, pi - 1)
                quick_sort_util(pi + 1, high)

        quick_sort_util(0, len(items) - 1)

        self.head = items[0] 
        for i in range(len(items) - 1):
            items[i].next = items[i + 1]
        items[-1].next = None


# Inisialisasi toko dan tambahkan barang
toko = TokoBangunan()
toko.tambah_barang_di_akhir(Barang(5, "Cat Tembok", 50000, 100, "Cat"))
toko.tambah_barang_di_akhir(Barang(6, "Paku", 1000, 200, "Perkakas"))
toko.tambah_barang_di_akhir(Barang(8, "Semenn", 75000, 100, "Material Bangunan"))
toko.tambah_barang_di_akhir(Barang(1, "Bor", 75000, 50, "Perkakas"))
toko.tambah_barang_di_akhir(Barang(3, "Pasir", 95000, 200, "Material bangunan "))
toko.tambah_barang_di_akhir(Barang(25, "Keramik", 10000, 1000, "Material Bangunan"))
toko.tambah_barang_di_akhir(Barang(10, "Bergaji", 35000, 20, "Perkakas"))

print(YELLOW +'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + RESET)
print(PINK + "Daftar Barang sebelum diurutkan:" + RESET)
print(YELLOW +'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + RESET)
toko.tampilkan_barang()
print(BLUE + "====================================================================================================" + RESET)

# Urutkan berdasarkan ID secara descending
toko.quick_sort('id_barang', order='descending')
print(YELLOW +'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + RESET)
print("\n" + PINK + "Daftar Barang setelah diurutkan berdasarkan ID secara descending:" + RESET)
print(YELLOW +'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + RESET)
toko.tampilkan_barang()
print(BLUE + "====================================================================================================" + RESET)

# Urutkan berdasarkan Nama secara ascending
toko.quick_sort('nama', order='ascending')
print(YELLOW +'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + RESET)
print("\n" + PINK + "Daftar Barang setelah diurutkan berdasarkan Nama secara ascending:" + RESET)
print(YELLOW +'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + RESET)
toko.tampilkan_barang()
print(BLUE + "====================================================================================================" + RESET)

# Mencari barang berdasarkan ID
search_result_id = toko.search_by_id(8)
print(YELLOW +'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + RESET)
print('\n' + PINK + "Serching Fibonacci Berdasarkan ID:" + RESET)
print(YELLOW +'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + RESET)
print(f"ID: {search_result_id.id_barang}, Nama: {search_result_id.nama}, Harga: {search_result_id.harga}, Stok: {search_result_id.stok}, Kategori: {search_result_id.kategori}")
print(BLUE + "====================================================================================================" + RESET)

# Mencari barang berdasarkan Nama
search_result_name = toko.search_by_name("Paku")
print(YELLOW +'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + RESET)
print('\n' + PINK + "Serching Fibonacci Berdasarkan Nama:" + RESET)
print(YELLOW +'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + RESET)
print(f"ID: {search_result_name.id_barang}, Nama: {search_result_name.nama}, Harga: {search_result_name.harga}, Stok: {search_result_name.stok}, Kategori: {search_result_name.kategori}")
print(BLUE + "====================================================================================================" + RESET)

# Menampilkan Stack
print(YELLOW +'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + RESET)
print(PINK + "Isi Stack:" + RESET)
print(YELLOW +'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + RESET)
toko.tampilkan_stack()
print(BLUE + "====================================================================================================" + RESET)

# Menampilkan Queue
print(YELLOW +'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + RESET)
print(PINK + "Isi Queue:" + RESET)
print(YELLOW +'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + RESET)
toko.tampilkan_queue()
print(BLUE + "====================================================================================================" + RESET)
