from turtle import title
from unicodedata import name
from django.test import TestCase
from Todo.models import Memorandum
from Todo.models import User
from Todo.models import Codebook
import datetime
class mytest(TestCase):
    def setUp(self) -> None:
        Memorandum.objects.create(title="aa1",content="aass",status=True,timeStamp="2022-12-11")
        User.objects.create(uid="asf",pwd="bb")
        Codebook.objects.create(tag="qq1",unm="aa",pwd="ss",tsp="2022-12-11")
    #create object
    def testcase1(self):
        Memorandum.objects.create(title="aa",content="aass",status=True,timeStamp="2022-12-11")
        p=Memorandum.objects.get(title="aa")
        self.assertEqual(p.title,"aa")
        self.assertEqual(p.content,"aass")
        self.assertEqual(p.status,True)
        self.assertEqual(p.timeStamp,datetime.datetime(2022, 12, 11, 0, 0, tzinfo=datetime.timezone.utc))
    def testcase2(self):
        User.objects.create(uid="aa",pwd="bb")
        u=User.objects.get(uid="aa")
        self.assertEqual(u.uid,"aa")
        self.assertEqual(u.pwd,"bb")
    def testcase3(self):
        Codebook.objects.create(tag="qq",unm="aa",pwd="ss",tsp="2022-12-11")
        p=Codebook.objects.get(tag="qq")
        self.assertEqual(p.tag,"qq")
        self.assertEqual(p.unm,"aa")
        self.assertEqual(p.pwd,"ss")
        self.assertEqual(p.tsp,datetime.date(2022, 12, 11))
    #delete test
    def test1delete(self):
        p=Memorandum.objects.get(title="aa1")
        p.delete()
        r=Memorandum.objects.filter(title="aa1")
        self.assertEqual(len(r),0)
    def test2delete(self):
        p=User.objects.get(uid="asf")
        p.delete()
        r=User.objects.filter(uid="asf")
        self.assertEqual(len(r),0)
    def test3delete(self):
        p=Codebook.objects.get(tag="qq1")
        p.delete()
        r=Codebook.objects.filter(tag="qq1")
        self.assertEqual(len(r),0)
    #update
    def test1update(self):
        p=Memorandum.objects.get(title="aa1")
        p.title="ajj"
        p.content="aa"
        p.save()
        r=Memorandum.objects.get(title="ajj")
        self.assertEqual(r.content,"aa")
        self.assertEqual(r.title,"ajj")
    def test2update(self):
        p=User.objects.get(uid="asf")
        p.uid="ssaa"
        p.pwd="123"
        p.save()
        r=User.objects.get(uid="ssaa")
        self.assertEqual(r.uid,"ssaa")
        self.assertEqual(r.pwd,"123")
    def test3update(self):
        p=Codebook.objects.get(tag="qq1")
        p.tag="qwq"
        p.save()
        r=Codebook.objects.get(tag="qwq")
        self.assertEqual(r.tag,"qwq")
