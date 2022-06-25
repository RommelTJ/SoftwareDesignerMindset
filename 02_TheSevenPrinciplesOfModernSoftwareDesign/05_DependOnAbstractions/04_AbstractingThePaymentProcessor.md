# Abstracting the Payment Processor

* See code example.
* The payment processor has a pay_debit, pay_credit methods that are very similar.
* Authorizations and Payment Types vary independently.
* The Bridge Pattern addresses this specifically.
  * We split each payment method into its own class.
  * If we need to add a new payment method, we simply create a new payment class.
