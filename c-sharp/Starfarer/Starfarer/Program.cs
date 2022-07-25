using System.Dynamic;
using static System.Console;

var s = "\\My Test\\\\";
char[] a = { '\\' };
WriteLine(s.LastIndexOfAny(a));

//WriteLine(decimal.MaxValue > long.MaxValue);

//public class A
//{
//    protected virtual void method()
//    {

//    }
//}


//public class B : A
//{
//    public static void method(int foo)
//    {

//    }
//}

//public record C
//{
//    public int foo;
//    public int moo;
//    //public string bah;
//    public void Test(C shape) 
//    { 
//        ExpandoObject.Remove()
//    }

//}

