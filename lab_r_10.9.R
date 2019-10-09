


# a<-c(1:10)
# sum(a)
# seq(1,100,by=1)
# sum(seq(1,100,by=1)*seq(1,100,by=1))


#task 2
# x<- seq(1,5,by=0.3)
# mean(x)
# sd(x)
# x.std<-(x-mean(x))/(sd(x))
# 
# set.seed(1)
# x<-rnorm(100,mean=1,sd=1)
# s_x_square<-(1/99)*sum((x-mean(x))^(2))
# t<-(100)^(1/2)*mean(x)/(s_x_square)


#task 4
#2046
# loop<-rep(0,10)
# task4<-seq(1,100,by=1)
# for(i in c(1:10))
# {
#   t=2^(i)
#   loop[i]=t
# }
# sum(loop)
# 
# #why int
# loop2<-rep(0,10000)
# task4_2<-seq(1,10000,by=1)
# for(i in c(1:10000))
# {
#   t=2^(i)
#   loop2[i]=t
# }
# sum(loop2)

# 
x<-rcauchy(100)
mean(x)
median(x)
new_x<-sort(x)[11:90]

# 
# x<-rnorm(100)
# x<-rcauchy(100)
u <- seq(1,100,by=1)
for (i in c(1:100))
{
if(u[i]<55) {
              u[i]=0
            } 
}

# else {
#   // statement(s) will execute if the boolean expression is false.
# # }//
# a<-c(TRUE,FALSE)
# b<-c(FALSE,FALSE)
# c<-(a & !b)
# d<-a|b

a<-seq(1,10,1)
b<-rep()

#task 9 
y <- matrix(1:25,nrow=5,ncol=5) 
y[1,]<-c(1,0,0,-1,0)
y[2,]<-c(0,5,0,0,0)
y[4,]<-c(0,0,0,7,0)
y[3,]<-c(3,0,1,0,0)
y[5,]<-c(0,0,0,0,9)
y
y[1:3,1:2]
y[y=0]<-1#####???????????????





A<- matrix(1:9,nrow=3,ncol=3) 
A[1,]<-c(1,2,3)
A[2,]<-c(2,20,26)
A[3,]<-c(3,26,70)
b<-c(4,52,31)
z<-solve(A)%*%b
#11.3
#chol(A) 下三角 L
#t(chol(A)) 上三角
t(chol(A))%*%chol(A)
chol(A)

#question 5 6 
v=forwardsolve(solve(chol(A)),b)
z=backsolve(t(chol(A)),v)
#question 7
chol(A)
det(A)



#task10
A<-matrix(rnorm(9e6),nrow=3e3)
B<-matrix(rnorm(9e6),nrow=3e3)
x<-rnorm(3e3)


A%*%(B%*%x)
time1 <- proc.time() 
(A%*%B)%*%x
time2 <-  proc.time() - time1 
time2
#task8
m<-c(1,2,3)
rep(m,4)

rep(1:3,each=2)
rep(2^(0:10))
rep((1:10)^(2))



