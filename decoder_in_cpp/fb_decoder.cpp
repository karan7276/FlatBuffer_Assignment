
#include "schema_generated.h"
#include <fstream>
#include <iostream>

int main(int argc, const char *argv[]) {
    // Read from bin file
    std::ifstream infile;
    infile.open("../fb_bytes.bin",std::ios::binary | std::ios::in);
    infile.seekg(0,std::ios::end);
    int length = infile.tellg();
    infile.seekg(0,std::ios::beg);
    char *data = new char[length];
    infile.read(data, length);
    infile.close();

    auto clients = GetClientList(data);
    auto clients_list = clients->clients();
    for(unsigned int i=0; i < clients_list->size();i++){
        auto client = clients_list->Get(i);
        auto isPerson = client->is_person();
        if(isPerson){
            auto person = client->person();
            auto person_name = person->name();
            auto person_age = person->age();
            auto person_weight = person->weight();
            auto person_gender = person->gender();
            std::cout<<"{ "<<person_name->str()<<","<<person_age<<","<<person_weight<<","<<person_gender->str()<<" }"<<std::endl;
        }else{
            auto group = client->group();
            auto groupname = group->groupname();
            auto average_age = group->average_age();
            auto average_weight = group->average_weight();
            
            std::cout<<"{ "<<groupname->str()<<","<<average_age<<","<<average_weight<<",";
            auto person_names = group->names();
            std::cout<<" {";
            for(unsigned int j=0; j<person_names->size()-1; j++){
                std::cout<<person_names->Get(j)->str()<<",";
            }
            std::cout<<person_names->Get(person_names->size()-1)->str()<<"}"<<" }";
        }
        
        
    }
    return 0;
}