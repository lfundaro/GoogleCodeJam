/*
 *  milk.cpp
 *  Constraint implementation of google code jam 2008 online round A
 *  problem "milkshakes"
 *  Google code jam warming up
 *
 *  Author: Javier Fernandez
 *          javierfdr@gmail.com
 */


#include <gecode/int.hh>
#include <gecode/minimodel.hh>
#include <gecode/driver.hh>
#include <time.h>
#include <fstream>
#include <string>
#include <algorithm>
#include <vector>
#include <stdlib.h>

using namespace Gecode;
using namespace std;

int numMilkShakes;
int numCustomers;
vector< vector<int> > c_likes;

class MilkShakes: public MinimizeScript {
protected:
  IntVarArray all_together;
  IntVarArray malted;
  IntVarArray unmalted;
  IntVar total_shakes;

public:

  MilkShakes(const Options& opt): malted(*this,numMilkShakes,0,1), unmalted(*this,numMilkShakes,0,1),total_shakes(*this,0,numMilkShakes),all_together(*this,numMilkShakes*2,0,1)
  {
    
    //set all_together
    for(int i=0;i<numMilkShakes;i++){
      post(*this,all_together[i]==malted[i]);
    }
    //set all_together
    for(int i=numMilkShakes;i<numMilkShakes*2;i++){
      post(*this,all_together[i]==unmalted[i-numMilkShakes]);
    }

    // Exactly one batch for each flavor
    for(int i=0;i<numMilkShakes;i++){
      post(*this,malted[i]+unmalted[i]==1);
    }

    //for each customer at least one mil shake they like
    //linking customer likes with variables
    vector< vector<int> >::iterator it;
    vector<int>:: iterator cit;
    vector<int> customer_likes;
    int index;
    int shake;

    for(it=c_likes.begin();it!=c_likes.end();it++){
      customer_likes=*it;     
      IntVarArgs customer_vars(customer_likes.size()/2);      
      int var_count=0;
      for(cit=customer_likes.begin();cit!=customer_likes.end();cit++){
	index = *cit;
	cit++;
	shake = *cit;
	if(shake==0){ //unmalted
	  customer_vars[var_count] = unmalted[index-1];
	}
	else if(shake ==1){//malted
	  customer_vars[var_count] = malted[index-1];
	}
	var_count++;
      }
      linear(*this,customer_vars,IRT_GQ,1);      
    }

    //cost function: number of malted shakes;
    linear(*this,malted,IRT_EQ,total_shakes);    
    
    
    VarBranchOptions varOpt= VarBranchOptions();
    ValBranchOptions valOpt =ValBranchOptions::time(); //Udpdating the seed
    //Define branching with opt.branching value and first-fail for variables
    branch(*this,all_together,INT_VAR_SIZE_MIN, IntValBranch(opt.branching()),varOpt,valOpt); 
  };

 // Definition of copy functions
  MilkShakes(bool share, MilkShakes& s) : MinimizeScript(share,s){

    all_together.update(*this,share,s.malted);
    malted.update(*this,share,s.malted);
    unmalted.update(*this,share,s.unmalted);
    total_shakes.update(*this,share,s.total_shakes);
  }  
  virtual Space* copy(bool share){
    return new MilkShakes(share,*this);
  }
  
  virtual IntVar cost(void) const {
    return total_shakes;
  }
  
  //Print to ostream 
  void print(std::ostream& os) const {
    os << malted << std::endl;
  }
};

  int main(int argc, char* argv[]){
    
    numMilkShakes = atoi(argv[1]);
    numCustomers = atoi(argv[2]);
    int c_argc = 3;
    int t;
    //Set c_likes (customer likes) array
    while(c_argc<argc){
      t= atoi(argv[c_argc]);c_argc+=1;
      vector<int> c = vector<int>();
      for(int i=0;i<t*2;i++){
	c.push_back(atoi(argv[c_argc]));c_argc+=1;
      }
      c_likes.push_back(c);    
    }
        
    Options opt("MilkShakes Solution");  
    opt.solutions(0); //default to first solution
    opt.parse(argc,argv);
  
    Script::run<MilkShakes,BAB,Options>(opt);
    return 0;
 }
