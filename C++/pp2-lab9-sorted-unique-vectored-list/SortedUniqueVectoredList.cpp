#include <stdexcept> // std::out_of_range
#include <utility>   // std::exchange
#include <array>
#include <limits>
#include <algorithm>
#include <string>
#include <stdexcept>
#include <vector>

#if __has_include("../SortedUniqueVectoredList.h")
    #include "../SortedUniqueVectoredList.h"
#elif __has_include("SortedUniqueVectoredList.h")
    #include "SortedUniqueVectoredList.h"
#else
    #error "File 'SortedUniqueVectoredList.h' not found!"
#endif

using namespace std;


/** class SortedUniqueVectoredList::Bucket
 * @param size ilosc elementow w kubelku, tworzac pusty ma byc 0
 * @param values elementy kubelka, jako tablica statyczna
 * @param BUCKET_SIZE ilosc elementow w statycznej tablicy
 * @param bucketCount_ ilosc kubelkow
 * @param next wskaznik na nastepny @ref Bucket, a jesli takiego nie ma na nullptr
 * @param previous wskaznik na poprzedni @ref Bucket, a jesli takiego nie ma na nullptr
 * @note jest to klasa zrobiona przy pomocy [idiomu PIMPL](https://en.cppreference.com/w/cpp/language/pimpl),
 *       ktory polega na tym, ze w klasie zewnetrznej jest jedynie deklaracja klasy wewnetrznej, ktora jest zaimplementowana w pliku zrodlowym **/
struct SortedUniqueVectoredList::Bucket
{
    constexpr static size_t BUCKET_SIZE = 10;

    std::array<std::string, BUCKET_SIZE> values;
    size_t size{};

    Bucket* next = nullptr;
    Bucket* previous = nullptr;
};


SortedUniqueVectoredList::SortedUniqueVectoredList(const SortedUniqueVectoredList &source)
{
    /// @todo zaimplementuj, szczegoly w pliku naglowkowym
    copy(source);

}

SortedUniqueVectoredList::SortedUniqueVectoredList(SortedUniqueVectoredList &&another)
{
    /// @todo zaimplementuj, szczegoly w pliku naglowkowym
    this->move(std::move(another));
}

SortedUniqueVectoredList::~SortedUniqueVectoredList()
{
    /// @todo zaimplementuj, szczegoly w pliku naglowkowym
    free();
}

SortedUniqueVectoredList &SortedUniqueVectoredList::operator=(SortedUniqueVectoredList &&another)
{
    /// @todo zaimplementuj, szczegoly w pliku naglowkowym
    if (this != &another)
    {
        this->move(std::move(another));
    }
    return *this;
}

void SortedUniqueVectoredList::insert(const std::string& value)
{
    if (contains(value)) return;


    std::vector<std::string> allValues;
    Bucket* current = head;
    while (current) {
        for (size_t i = 0; i < current->size; ++i)
            allValues.push_back(current->values[i]);
        current = current->next;
    }

    allValues.push_back(value);

    std::sort(allValues.begin(), allValues.end());

    free(); 

    for (const std::string& val : allValues) {
        if (!head) {
            head = new Bucket();
            tail = head;
            bucketCount_ = 1;
            capacity_ = Bucket::BUCKET_SIZE;
        }
        if (tail->size == Bucket::BUCKET_SIZE) {
            Bucket* newBucket = new Bucket();
            tail->next = newBucket;
            newBucket->previous = tail;
            tail = newBucket;
            bucketCount_++;
            capacity_ += Bucket::BUCKET_SIZE;
        }
        tail->values[tail->size++] = val;
        size_++;
    }
}

void SortedUniqueVectoredList::erase(const string &value)
{
    /// @todo zaimplementuj, szczegoly w pliku naglowkowym (opcjonalne zadanie)
    Bucket* current = head;
    while (current) {
        for (size_t i = 0; i < current->size; ++i) {

            if (current->values[i] == value) {
                for (size_t j = i; j < current->size; ++j) {
                    current->values[j] = current->values[j + 1];
                }
                current->size--;
                size_--;
                current->values[current->size].clear();

            }

        }

        current = current->next;
    }
}

SortedUniqueVectoredList::operator std::string() const
{
    string result="";
    Bucket* current = head;
    while (current) {
        for (size_t i = 0; i < current->size; ++i) {
            result += current->values[i];
        }
        current = current->next;
    }
    return result;
}

void SortedUniqueVectoredList::allocate_new_bucket()
{
    /// @todo zaimplementuj, szczegoly w pliku naglowkowym

    Bucket* newBucket = new Bucket();
    newBucket->size = 0;
    newBucket->next = nullptr;
    newBucket->previous = tail;

    if (tail) {
        tail->next = newBucket;
    } else {
        head = newBucket;
    }

    tail = newBucket;


    capacity_ += Bucket::BUCKET_SIZE;
    bucketCount_++;
}

void SortedUniqueVectoredList::free()
{
    /// @todo zaimplementuj, szczegoly w pliku naglowkowym
    Bucket* curr = head;
    while (curr != nullptr) {
        Bucket* next = curr->next;
        delete curr;
        curr = next;
    }
    head = nullptr;
    bucketCount_ = 0;
    capacity_ = 0;
    size_=0;
    tail=nullptr;
}

void SortedUniqueVectoredList::move(SortedUniqueVectoredList &&another)
{
    /// @todo zaimplementuj, szczegoly w pliku naglowkowym
    head = another.head;
    tail = another.tail;
    capacity_ = another.capacity_;
    bucketCount_ = another.bucketCount_;
    size_ = another.size_;
    another.head = nullptr;
    another.tail = nullptr;
    another.capacity_ = 0;
    another.size_ = 0;
    another.bucketCount_ = 0;
}

void SortedUniqueVectoredList::copy(const SortedUniqueVectoredList &other)
{
    /// @todo zaimplementuj, szczegoly w pliku naglowkowym
    head = tail = nullptr;
    size_ = capacity_ = bucketCount_ = 0;

    Bucket* otherBucket = other.head;
    Bucket* prev = nullptr;

    while (otherBucket) {
        Bucket* nowy = new Bucket();
        nowy->size = otherBucket->size;
        for (size_t i = 0; i < nowy->size; ++i)
            nowy->values[i] = otherBucket->values[i];

        if (!head) head = nowy;
        if (prev) {
            prev->next = nowy;
            nowy->previous = prev;
        }

        tail = nowy;
        prev = nowy;

        size_ += nowy->size;
        capacity_ += Bucket::BUCKET_SIZE;
        bucketCount_++;

        otherBucket = otherBucket->next;
    }
    }




bool SortedUniqueVectoredList::contains(const string &value) const
{
    /// @todo zaimplementuj, szczegoly w pliku naglowkowym
    Bucket* current = head;
    while (current) {
        for (size_t i = 0; i < current->size; ++i) {
            if (current->values[i] == value) return true;
        }
        current = current->next;
    }
    return false;
}

SortedUniqueVectoredList SortedUniqueVectoredList::operator-(const SortedUniqueVectoredList &another) const
{
    SortedUniqueVectoredList result;

    Bucket* current = this->head;
    while (current) {
        for (size_t i = 0; i < current->size; ++i) {
            const std::string& val = current->values[i];
            if (!another.contains(val)) {
                result.insert(val);
            }
        }
        current = current->next;
    }

    return result;
}
SortedUniqueVectoredList &SortedUniqueVectoredList::operator*=(const size_t howManyTimesMultiply)
{
    /// @todo zaimplementuj, szczegoly w pliku naglowkowym
    Bucket* current = head;
    while (current) {
        for (size_t i = 0; i < current->size; ++i) {
            string text = current->values[i];
            string result = "";
            for (size_t j = 0; j < howManyTimesMultiply; ++j) {
                result += text;
            }
            current->values[i] = result;
        }
        current = current->next;
    }
    return *this;
}

string &SortedUniqueVectoredList::operator[](size_t index)
{
    /// @todo zaimplementuj, szczegoly w pliku naglowkowym
    if (index >= size_) throw out_of_range("Index out of range");
    Bucket* curr = head;
    while (curr != nullptr) {
        if (index < curr->size) {
            return curr->values[index];
        }else {
            index -= curr->size;
            curr = curr->next;
        }
    }
    throw std::out_of_range("");
}

const string& SortedUniqueVectoredList::operator[](size_t index) const
{
    /// @todo zaimplementuj, szczegoly w pliku naglowkowym
    if (index >= size_) throw out_of_range("Index out of range");
    Bucket* curr = head;
    while (curr != nullptr) {
        if (index < curr->size) {
            return curr->values[index];
        }else {
            index -= curr->size;
            curr = curr->next;
        }
    }
    throw std::out_of_range("");
}

SortedUniqueVectoredList &SortedUniqueVectoredList::operator=(const SortedUniqueVectoredList &another)
{
    /// @todo zaimplementuj, szczegoly w pliku naglowkowym
    if (this!=&another) {
        free();
        copy(another);
    }
    return *this;
}
