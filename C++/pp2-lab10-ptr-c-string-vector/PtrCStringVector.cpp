#include <functional>
#include <algorithm>
#include <string>
#include <cstring>
#include <stdexcept>
#include <utility> // std::exchange
#include "PtrCStringVector.h"
using namespace std;


PtrCStringVector::PtrCStringVector()
{
    /// @todo zaimplementuj, szczegoly w pliku naglowkowym
    /** @brief konstruktor domyslny, jego zadaniem jest ustawienie size_, capacity_ i data_ na brak elementow **/
    size_=0;
    capacity_=0;
    data_=nullptr;

}

PtrCStringVector::PtrCStringVector(const PtrCStringVector &srcPtrCStringVector): PtrCStringVector()
{
    /// @todo zaimplementuj, szczegoly w pliku naglowkowym
    size_=srcPtrCStringVector.size();
    capacity_=srcPtrCStringVector.capacity();
    data_=new char*[capacity_];
    for(size_t i=0;i<size_;i++) {
        if(srcPtrCStringVector.data_!=nullptr) {
            data_[i]=new char[strlen(srcPtrCStringVector.data_[i])+1];
            strcpy(data_[i],srcPtrCStringVector.data_[i]);
        }
        else {
            data_[i]=nullptr;
        }
    }

}

PtrCStringVector::~PtrCStringVector()
{
    /// @todo zaimplementuj, szczegoly w pliku naglowkowym
    if (data_!=nullptr) {
        for(size_t i=0;i<size_;i++) {
                delete[] data_[i];
        }
        delete[] data_;
        data_=nullptr;
    }
    size_=0;
    capacity_=0;
}

PtrCStringVector &PtrCStringVector::operator=(const PtrCStringVector &source)
{
    /// @todo zaimplementuj, szczegoly w pliku naglowkowym
    if (this == &source) return *this;
    if (data_!=nullptr) {
        for(size_t i=0;i<size_;i++) {
            delete[] data_[i];
        }
        delete[] data_;
        data_=nullptr;
    }
    size_=source.size();
    capacity_=source.capacity();
    data_=new char*[source.capacity()];

    for(size_t i=0;i<size_;i++) {
        if(source.data_!=nullptr) {
            data_[i]=new char[strlen(source.data_[i])+1];
            strcpy(data_[i],source.data_[i]);
        }else {
            data_[i]=nullptr;
        }

    }

    return *this;
}

PtrCStringVector& PtrCStringVector::operator=(PtrCStringVector&& source)
{
    if (this == &source)
        return *this;
    free();
    size_ = source.size_;
    capacity_ = source.capacity_;
    data_ = source.data_;
    source.size_ = 0;
    source.capacity_ = 0;
    source.data_ = nullptr;
    return *this;
}

void PtrCStringVector::push_back(const char *text2Add)
{
    if (text2Add == nullptr) {
        text2Add = "";  // lub zwróć wyjątek, jeśli nie akceptujesz nullptr
    }
    /// @todo zaimplementuj, szczegoly w pliku naglowkowym
    if (size_==capacity_) {
        if (capacity_==0) {
            reserve(10);
        }
        reserve(capacity_*2);
    }
    data_[size_]=new char[strlen(text2Add)+1];
    strcpy(data_[size_],text2Add);
    size_++;

}

PtrCStringVector PtrCStringVector::operator+(const PtrCStringVector &anotherVector) const
{
    /// @todo zaimplementuj, szczegoly w pliku naglowkowym
    PtrCStringVector resultVector;
    resultVector.size_=size_+anotherVector.size();
    resultVector.capacity_=capacity_+anotherVector.capacity();
    resultVector.data_=new char*[resultVector.capacity()];
    for(size_t i=0;i<size_;i++) {
        resultVector.data_[i] = new char[strlen(data_[i])+1];
        strcpy(resultVector.data_[i],data_[i]);
    }
    for(size_t i=0;i<anotherVector.size();i++) {
        resultVector.data_[i+size_] = new char[strlen(anotherVector.data_[i])+1];
        strcpy(resultVector.data_[i+size_],anotherVector.data_[i]);
    }
    return resultVector;
}

char *PtrCStringVector::operator[](std::size_t index)
{
    /// @todo zaimplementuj, szczegoly w pliku naglowkowym
    if (index >= size_) {
        throw std::out_of_range("idx out of range");
    }
    return data_[index];
    //return new char[1]{};
}
const char *PtrCStringVector::operator[](std::size_t index) const
{
    if (index >= size_) {
        throw std::out_of_range("idx out of range");
    }
    return data_[index];
}

PtrCStringVector PtrCStringVector::operator&(const PtrCStringVector &rhs) const
{
    PtrCStringVector resultVector;
    resultVector.size_ = std::max(size_, rhs.size());
    resultVector.capacity_ = resultVector.size_;
    resultVector.data_ = new char*[resultVector.capacity_];

    for (size_t i = 0; i < resultVector.size_; ++i) {
        const char* left = (i < size_ && data_[i]) ? data_[i] : nullptr;
        const char* right = (i < rhs.size_ && rhs.data_[i]) ? rhs.data_[i] : nullptr;

        if (left && right) {
            resultVector.data_[i] = new char[strlen(left) + strlen(right) + 1];
            strcpy(resultVector.data_[i], left);
            strcat(resultVector.data_[i], right);
        } else if (left) {
            resultVector.data_[i] = new char[strlen(left) + 1];
            strcpy(resultVector.data_[i], left);
        } else if (right) {
            resultVector.data_[i] = new char[strlen(right) + 1];
            strcpy(resultVector.data_[i], right);
        } else {
            resultVector.data_[i] = nullptr;
        }
    }

    return resultVector;
}

void PtrCStringVector::free()
{
    /// @todo sugeruje zaimplementowac, szczegoly w pliku naglowkowym
    if (data_!=nullptr) {
        for(size_t i=0;i<size_;i++) {
                delete[] data_[i];
        }
        delete[] data_;
    }
    size_=0;
    capacity_=0;
    data_=nullptr;
}

void PtrCStringVector::reserve(std::size_t new_capacity)
{
    /// @todo sugeruje zaimplementowac, szczegoly w pliku naglowkowym
    if (new_capacity <= capacity_)
        return;  // Nie trzeba rezerwować mniej lub tyle samo
    char** tempdata=new char*[new_capacity];
    if(data_!=nullptr) {
    for(size_t i=0;i<size_;i++) {
            tempdata[i]=data_[i];
        }
    }
    delete[] data_;
    data_ = tempdata;
    capacity_=new_capacity;
}
