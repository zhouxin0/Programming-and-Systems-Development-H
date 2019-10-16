getwd()
setwd("/Users/marco/Archive")
health<-read.table('health.txt')
cia<-read.csv('cia.csv',na.strings = "?")
#write.table
write.table(health, file = "health.txt",sep = " ", na = "*", row.names = c(1:170),col.names = c('1','2','3','4','5','6'))

speed<-c(34,49,52,24,60,74,55)
speed.discretised<-cut(speed,breaks = 3)
speed.discretised<-cut(speed,breaks=c(0,40,60,100),labels=c('slow','medium','fast'))
health
health.n<-as.numeric(health$V5[-1])
health.discretised<-cut(health.n,breaks=c(0,40,70,200),labels=c('low','medium','high'))
#health[,5]
maternity<-read.csv('maternity.csv')
m_q1<- maternity$Maternities-maternity$SmokingUnknown
m_q1.2<-maternity$Maternities-maternity$BreastfeedingUnknown
prop_smoking_preg<-maternity$Smoking/m_q1
prop_breastfeeding_preg<-maternity$Breastfeeding/m_q1.2
intersection<-cbind(prop_smoking_preg,prop_breastfeeding_preg)
maternity_new<-cbind(maternity,intersection)
which.max(maternity_new$prop_smoking_preg)
which.max(maternity_new$prop_breastfeeding_preg)
which.min(maternity_new$prop_smoking_preg)
which.min(maternity_new$prop_breastfeeding_preg)
maternity_new[32,]

maternity_new[13,]
maternity_new[56,]
maternity_new[37,]


#q3
maternity_new[maternity_new$Region==c('London','North West'),]

maternity_new[maternity_new$Deprivation>40|maternity_new$Deprivation<10,]

#maternity_new[maternity_new$Deprivation<10|maternity_new$>40,]


#q5
cia_new<-cia[complete.cases(cia$Population),]
small<-cia_new[cia_new$Population<10000,]
#military at least 8%
lowexp<-(cia_new$MilitaryExpenditure/cia_new$GDP)>0.08
names(cia_new)
cia_new$Country[lowexp] 
#Iraq Jordan Qatar Oman Saudi Arabia
cia_new$Country

sum_eurogdp<-na.omit(cia_new[cia$Continent=='Europe',])
sum(sum_eurogdp$GDP) #1.113595e+13

#5
cia_new2<-cia_new[complete.cases(cia_new$GDP),]
cia_new_n<-cia_new[complete.cases(cia_new$MilitaryExpenditure),]
GDPPerCapita<-cia_new_n$GDP/cia_new_n$Population
MilitaryExpenditurePerCapita<-cia_new_n$MilitaryExpenditure/cia_new_n$Population
ooo<-cbind(GDPPerCapita,MilitaryExpenditurePerCapita)
cia_new_n_n<-cbind(cia_new_n,ooo)
cia
which.max(cia$Life)
cia[138,]
top_ten_temp<-cia[order(cia$Life),]
topten<-top_ten_temp[1:10,]
nona_life<-na.omit(top_ten_temp)
tail(nona_life,n = 10)
###task 6 
alligator<-read.csv('alligator.csv')
x<-alligator$Length
y <- alligator$Weight

x_mean<-sum(x)/15
y_mean<-sum(y)/15
x_m<-rep(x_mean,15)
y_m<-rep(y_mean,15)
beta_hat_1<-sum((x-x_m)*(y-y_m))/sum((x-x_m)*(x-x_m))
beta_hat_0 <- y_mean-beta_hat_1*x_mean
y_hat <- beta_hat_0+beta_hat_1*x
#variance
sum((y-y_hat)^2)/(15-2)
R_square <- 1-sum((y-y_hat)^2)/sum((y-y_m)^2)

lm_alligator<- lm(y~x,data=alligator) 
summary(lm_alligator)

#q3
X<-matrix(c(rep(1,15),c(x)),ncol = 2)
XtX<-t(X)%*%(X)
Xty<-t(X)%*%y
final<-solve(XtX)%*%Xty


