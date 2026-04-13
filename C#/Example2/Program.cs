using System.Xml.Schema;

wczytywacz wcz = new wczytywacz();

List<employee> pracownicy = wcz.wczytajListe("employees.csv", x => new employee(
    x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9],
     x[10], x[11], x[12], x[13], x[14], x[15], x[16], x[17]));
List<employee_territory> terytoriaPracownikow = wcz.wczytajListe("employee_territories.csv", x => new employee_territory(x[0], x[1]));
List<territory> terytoria = wcz.wczytajListe("territories.csv", x => new territory(x[0], x[1], x[2]));
List<region> regiony = wcz.wczytajListe("regions.csv", x => new region(x[0], x[1]));
List<order_details> detaleZamowien = wcz.wczytajListe("orders_details.csv", x => new order_details(
    x[0], x[1], x[2], x[3], x[4]));

List<order> zamowienia = wcz.wczytajListe("orders.csv", x => new order(
    x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9], 
    x[10], x[11], x[12], x[13]));

List<string> listaNazwisk = pracownicy.Select(x => x.lastname).ToList();

Console.WriteLine("Lista nazwisk:");
foreach (var nazwa in listaNazwisk)
{
    Console.WriteLine(nazwa);
}
Console.WriteLine("__________________");
var zapytanie = from p in pracownicy
                join tp in terytoriaPracownikow on p.employeeid equals tp.employeeid
                join t in terytoria on tp.territoryid equals t.territoryid
                join r in regiony on t.regionid equals r.regionid
                select new
{
    Nazwisko=p.lastname,
    Region = r.regiondescription,
    Terytorium = t.territorydescription
};

foreach (var rekord in zapytanie)
{
    Console.WriteLine($"Nazwisko: {rekord.Nazwisko} | Region: {rekord.Region} | Terytorium: {rekord.Terytorium}");
};
Console.WriteLine("__________________");

var zapytanie2 = from p in pracownicy
                join tp in terytoriaPracownikow on p.employeeid equals tp.employeeid
                join t in terytoria on tp.territoryid equals t.territoryid
                join r in regiony on t.regionid equals r.regionid
                group p.lastname by r.regiondescription into grupa
                select new
                {
                  Region = grupa.Key,
                  Pracownicy  = grupa.Distinct().ToList()
                };

foreach (var rekord in zapytanie2)
{
    Console.WriteLine($"Region: {rekord.Region} :");
    foreach ( var pracownik in rekord.Pracownicy)
    {
        Console.WriteLine($"        {pracownik}");
    }
};

Console.WriteLine("__________________");
foreach (var rekord in zapytanie2)
{
    Console.WriteLine($"Region: {rekord.Region} :");
    Console.WriteLine($"        {rekord.Pracownicy.Count}");
};
Console.WriteLine("__________________");



var wartosciZamowien = from d in detaleZamowien
                       group d by d.orderid into g
                       select new
                       {
                           OrderID = g.Key,
                           Wartosc = g.Sum(x => 
                               double.Parse(x.unitprice, System.Globalization.CultureInfo.InvariantCulture) * double.Parse(x.quantity, System.Globalization.CultureInfo.InvariantCulture) * (1 - double.Parse(x.discount, System.Globalization.CultureInfo.InvariantCulture)))
                       };


var zapytanie3 = from p in pracownicy
                join z in zamowienia on p.employeeid equals z.employeeid
                join w in wartosciZamowien on z.orderid equals w.OrderID
                group w by p.lastname into grupa 
                select new
                {
                  Nazwisko = grupa.Key,
                  LiczbaZamowien = grupa.Count(),
                  SredniaWartosc = grupa.Average(x=>x.Wartosc),
                  MaksymalnaWartosc = grupa.Max(x=>x.Wartosc),
                };

foreach (var rekord in zapytanie3)
{
    Console.WriteLine($"    Pracownik: {rekord.Nazwisko}");
    Console.WriteLine($"    Liczba zamówień: {rekord.LiczbaZamowien}");
    Console.WriteLine($"    Średnia wartość: {rekord.SredniaWartosc:F2}");
    Console.WriteLine($"     Max zamówienie : {rekord.MaksymalnaWartosc:F2}");
    Console.WriteLine("__________________");
}
struct order_details
{
    public string orderid { get; set; }
    public string productid { get; set; }
    public string unitprice { get; set; }
    public string quantity { get; set; }
    public string discount { get; set; }

    public order_details(string o_id, string p_id, string price, string qty, string disc)
    {
        orderid = o_id;
        productid = p_id;
        unitprice = price;
        quantity = qty;
        discount = disc;
    }
}

struct order
{
    public string orderid { get; set; }
    public string customerid { get; set; }
    public string employeeid { get; set; }
    public string orderdate { get; set; }
    public string requireddate { get; set; }
    public string shippeddate { get; set; }
    public string shipvia { get; set; }
    public string freight { get; set; }
    public string shipname { get; set; }
    public string shipaddress { get; set; }
    public string shipcity { get; set; }
    public string shipregion { get; set; }
    public string shippostalcode { get; set; }
    public string shipcountry { get; set; }

    public order(string o_id, string c_id, string e_id, string o_date, string r_date, string s_date, string s_via, string fr, string s_name, string s_addr, string s_city, string s_region, string s_postal, string s_country)
    {
        orderid = o_id;
        customerid = c_id;
        employeeid = e_id;
        orderdate = o_date;
        requireddate = r_date;
        shippeddate = s_date;
        shipvia = s_via;
        freight = fr;
        shipname = s_name;
        shipaddress = s_addr;
        shipcity = s_city;
        shipregion = s_region;
        shippostalcode = s_postal;
        shipcountry = s_country;
    }
}

class region
{
    public string regionid { get; set; }
    public string regiondescription { get; set; }

    public region(string id, string description)
    {
        regionid = id;
        regiondescription = description;
    }
}

class territory
{
    public string territoryid { get; set; }
    public string territorydescription { get; set; }
    public string regionid { get; set; }

    public territory(string t_id, string t_desc, string r_id)
    {
        territoryid = t_id;
        territorydescription = t_desc;
        regionid = r_id;
    }
}

class employee_territory
{
    public string employeeid { get; set; }
    public string territoryid { get; set; }

    public employee_territory(string e_id, string t_id)
    {
        employeeid = e_id;
        territoryid = t_id;
    }
}

class employee
{
    public string employeeid { get; set; }
    public string lastname { get; set; }
    public string firstname { get; set; }
    public string title { get; set; }
    public string titleofcourtesy { get; set; }
    public string birthdate { get; set; }
    public string hiredate { get; set; }
    public string address { get; set; }
    public string city { get; set; }
    public string region { get; set; }
    public string postalcode { get; set; }
    public string country { get; set; }
    public string homephone { get; set; }
    public string extension { get; set; }
    public string photo { get; set; }
    public string notes { get; set; }
    public string reportsto { get; set; }
    public string photopath { get; set; }

    public employee(string id, string lastName, string firstName, string empTitle, string courtesy, string birth, string hire, string addr, string empCity, string empRegion, string postal, string empCountry, string phone, string ext, string empPhoto, string empNotes, string reports, string photoPath)
    {
        employeeid = id;
        lastname = lastName;
        firstname = firstName;
        title = empTitle;
        titleofcourtesy = courtesy;
        birthdate = birth;
        hiredate = hire;
        address = addr;
        city = empCity;
        region = empRegion;
        postalcode = postal;
        country = empCountry;
        homephone = phone;
        extension = ext;
        photo = empPhoto;
        notes = empNotes;
        reportsto = reports;
        photopath = photoPath;
    }
}

class wczytywacz
{
    public List<T> wczytajListe<T>(string path, Func<string[], T> generuj)
    {
        List <T> lista= new List<T>();
        string[] linie = System.IO.File.ReadAllLines(path);

        for (int i = 1; i < linie.Length; i++)
        {
            string[] pola = linie[i].Split(',');
            T obiekt= generuj(pola);
            lista.Add(obiekt);
        }
        return lista;
    }
}

