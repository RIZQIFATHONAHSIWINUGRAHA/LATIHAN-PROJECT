#include <stdio.h>
#include <conio.h>
#include <iostream.h>


   char nama[50] ;
	int jumlah,diskon;
main(){

   cout<<"Masukkan Nama Team : ";gets(nama);
   cout <<"Berapa Jumlah Anggota : ";cin>>jumlah;
   if (jumlah >= 10 ){
   	diskon = jumlah - 3;
   	cout<<"Selamat anda dapat Potongan 3 Ticket saja";
   }else if (jumlah >= 5 ) {
   	diskon = jumlah - 1;
      cout<<"Selamat anda dapat Potongan 1 Ticket saja";
   }else {
      cout<<"Maaf anda tidak mendapat Gratis Ticket";
   }
   clrscr();
      cout <<"Hai Team " <<nama <<endl;
      cout <<"Anggota anda berjumlah : "<<jumlah  <<" Personil "<<endl;
      cout <<"Dan  kami informasikan bahwa anda hanya Perlu bayar " <<diskon
      <<" Ticket saja";
   getch();
}