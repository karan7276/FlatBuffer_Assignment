
import flatbuffers

import Person
import Group
import Client
import ClientList

builder = flatbuffers.Builder(1024)

# create person
male = builder.CreateString("Male")
female = builder.CreateString("Female")
name = builder.CreateString("Ram")

Person.Start(builder)
Person.AddName(builder,name)
Person.AddAge(builder,21)
Person.AddWeight(builder,76.5)
Person.AddGender(builder,male)
person_ram = Person.End(builder)

# create group
name2 = builder.CreateString("Shyam")
name3 = builder.CreateString("Raghuveer")
Group.StartNamesVector(builder,3)
builder.PrependUOffsetTRelative(name)
builder.PrependUOffsetTRelative(name2)
builder.PrependUOffsetTRelative(name3)
group_person_names = builder.EndVector()

group_name = builder.CreateString("FightClub")
Group.Start(builder)
Group.AddNames(builder,group_person_names)
Group.AddAverageAge(builder,24.5)
Group.AddAverageWeight(builder,66)
Group.AddGroupname(builder,group_name)
group1 = Group.End(builder)

Client.Start(builder)
Client.AddPerson(builder,person_ram)
Client.AddIsPerson(builder,True)
client1 = Client.End(builder)

Client.Start(builder)
Client.AddGroup(builder,group1)
Client.AddIsPerson(builder,False)
client2 = Client.End(builder)

ClientList.StartClientsVector(builder,2)
builder.PrependUOffsetTRelative(client2)
builder.PrependUOffsetTRelative(client1)
lists = builder.EndVector()

ClientList.Start(builder)
ClientList.AddClients(builder,lists)
clients = ClientList.End(builder)

builder.Finish(clients)

buffer = builder.Output()

open('../fb_bytes.bin','wb').write(buffer);