# Wallet_REST_test
Тестовое задание на позицию  Python developer.

**Задание:**
Пишем простой REST сервис (на Django).
Подразумевается, что под ваш REST сервис будет написано отдельное приложение (SPA или мобильное).

**Сервис по управлению финансами, функционал следующий:**
- Пользователь хранит данные о своем "кошельке", произвольное название + баланс в рублях.
- В рамках кошелька ведется история транзакций (как списание, так и пополнение).
- Кошельков может быть больше чем 1, но сам пользователь один (это его персональный веб сервис).

**API сервиса должен позволять:**
1. создавать, редактировать и удалять кошелек.
2. создавать и удалять транзакции в рамках кошелька (при этом напрямую редактировать баланс кошелька пользователь не может)
транзакции могут быть как +, так и -. то есть транзакции по зачислению денег и списанию.
у каждой транзакции должна быть дата, сумма, произвольный комментарий от пользователя.
3. Просматривать список своих кошельков
4. Просматривать список своих транзакций как в рамках одного кошелька, так и общий, всех кошельков сразу.
