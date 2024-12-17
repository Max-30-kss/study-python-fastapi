from abc import ABC, abstractmethod

# Інтерфейс для функцій друку
class PrinterInterface(ABC):
    @abstractmethod
    def print_document(self, document: str):
        pass

# Інтерфейс для функцій сканування
class ScannerInterface(ABC):
    @abstractmethod
    def scan_document(self) -> str:
        pass

# Інтерфейс для функцій копіювання
class CopierInterface(ABC):
    @abstractmethod
    def copy_document(self, document: str) -> str:
        pass

# Клас Принтер, реалізує тільки методи для друку
class Printer(PrinterInterface):
    def print_document(self, document: str):
        print(f"Printing document: {document}")

# Клас Сканер, реалізує тільки методи для сканування
class Scanner(ScannerInterface):
    def scan_document(self) -> str:
        scanned_document = "Scanned content"
        print("Scanning document...")
        return scanned_document

# Клас Мультифункціональний принтер, який реалізує всі методи
class MultiFunctionPrinter(PrinterInterface, ScannerInterface, CopierInterface):
    def print_document(self, document: str):
        print(f"Printing document: {document}")
    
    def scan_document(self) -> str:
        scanned_document = "Scanned content"
        print("Scanning document...")
        return scanned_document
    
    def copy_document(self, document: str) -> str:
        copied_document = f"Copy of {document}"
        print(f"Copying document: {document}")
        return copied_document

# Тестування
printer = Printer()
printer.print_document("Report")

scanner = Scanner()
scanned = scanner.scan_document()

mfp = MultiFunctionPrinter()
mfp.print_document("Photo")
mfp.scan_document()
mfp.copy_document("Report")