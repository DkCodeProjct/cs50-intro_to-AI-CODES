# Shopping Project cs50AI

### I enjoye Coding/solving this Project/.

  * in load Data func  i gotta  convert str row to int/float data points.
  actually ive done it before cos i wrote/do project before hand do the shopping project, in that project i did data cleaning: swap the row of data,
  data Label: put 0/1 in true/false , so it didnt bother me that much

  * firslty i tried to do like this:
    
    
-----------------------------------       
      
        if row['Month'] == 'Jan':
            month = 0
        
        elif row['Month'] == 'Feb':
            month = 1
        
        adminDuration = float(row['Administrative_Duration'])
        infoDuration = float(row['Informational_Duration'])
        productDuration = float(row['ProductRelated_Duration'])
        bounceRate = float(row['BounceRates'])
        exitRate = float(row['ExitRates'])
                
----------------------------------

  * which is very Unclever and messy,, however i ask duck debuger how to do this cleveryly he recon me to do like this:

  -  int(row['TrafficType']),
  -  1 if row['VisitorType'] == 'Returning_Visitor' else 0,

    * i knew this 1 if .. else 0 syntax but i was naive to apply finaly done it...!


### Func def evaluate(labels, predictions):

  * this func tell how well our model performe `identifying positive and negative cases`.

#### sensitivity, specificity | 
  *   |[Sensitivity]:
        + refers to the p`roportion of positive examples that were correctly identified` in other words, the proportion          of users` who did go through with a purchase` who were correctly identified. 
    
   

        + refers to the proportion of `negative examples that were correctly identified` in this case, the proportion of         users `who did not go through with a purchase` who were correctly identifi

+ how to calculate sensitivity/specifity:
 |[Specificity]:![Screenshot 2024-08-06 at 12-19-25 Confusion Matrix Explained](https://github.com/user-attachments/assets/9704ea3f-a15e-433c-8725-647d84c3e046)
  
