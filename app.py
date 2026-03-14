import streamlit as st

# ---------------- BANK CLASS ----------------
class BankApplication:
    bank_name = "SBI"

    def __init__(self, name, account_number, age, mobile_number, balance):
        self.name = name
        self.account_number = account_number
        self.age = age
        self.mobile_number = mobile_number
        self.balance = balance

    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
            return f"Transaction Successful. Collected ₹{amount}"
        else:
            return "Insufficient Balance"

    def deposit(self, amount):
        self.balance += amount
        return f"Deposit Successful. Total Balance: ₹{self.balance}"

    def update_mobile(self, new_number):
        self.mobile_number = new_number
        return f"Mobile number updated: {self.mobile_number}"

    def check_balance(self):
        return f"Total Account Balance: ₹{self.balance}"


# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="SBI Bank",
    page_icon="🏦",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

.main {
    background-color:#f4f6fb;
}

.title{
    font-size:40px;
    font-weight:bold;
    color:#1f4e79;
}

.card{
    background:white;
    padding:25px;
    border-radius:15px;
    box-shadow:0px 4px 10px rgba(0,0,0,0.1);
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown('<p class="title">🏦 SBI Digital Bank</p>', unsafe_allow_html=True)

# ---------------- SESSION ----------------
if "account" not in st.session_state:
    st.session_state.account = None

# ---------------- SIDEBAR ----------------
menu = [
    "Dashboard",
    "Create Account",
    "Deposit",
    "Withdraw",
    "Update Mobile",
    "Check Balance"
]

choice = st.sidebar.selectbox("🏦 Banking Menu", menu)

# ---------------- DASHBOARD ----------------
if choice == "Dashboard":

    st.header("📊 Bank Dashboard")

    if st.session_state.account:

        acc = st.session_state.account

        col1, col2, col3 = st.columns(3)

        col1.metric("💰 Balance", f"₹{acc.balance}")
        col2.metric("👤 Account Holder", acc.name)
        col3.metric("📱 Mobile", acc.mobile_number)

        st.markdown("### 💳 Account Card")

        st.markdown(f"""
        <div class="card">
        <h3>{BankApplication.bank_name} Bank</h3>
        <p><b>Name:</b> {acc.name}</p>
        <p><b>Account Number:</b> {acc.account_number}</p>
        <p><b>Balance:</b> ₹{acc.balance}</p>
        </div>
        """, unsafe_allow_html=True)

    else:
        st.info("Create an account to view dashboard")

# ---------------- CREATE ACCOUNT ----------------
elif choice == "Create Account":

    st.header("🆕 Create New Account")

    name = st.text_input("Enter Name")
    account_number = st.text_input("Account Number")
    age = st.number_input("Age", min_value=18)
    mobile = st.text_input("Mobile Number")
    balance = st.number_input("Initial Balance", min_value=0)

    if st.button("Create Account"):

        st.session_state.account = BankApplication(
            name,
            account_number,
            age,
            mobile,
            balance
        )

        st.success("✅ Account Created Successfully!")

# ---------------- DEPOSIT ----------------
elif choice == "Deposit":

    st.header("💰 Deposit Money")

    if st.session_state.account:

        amount = st.number_input("Enter Deposit Amount", min_value=1)

        if st.button("Deposit"):
            result = st.session_state.account.deposit(amount)
            st.success(result)

    else:
        st.warning("⚠ Create an account first")

# ---------------- WITHDRAW ----------------
elif choice == "Withdraw":

    st.header("💸 Withdraw Money")

    if st.session_state.account:

        amount = st.number_input("Enter Withdrawal Amount", min_value=1)

        if st.button("Withdraw"):
            result = st.session_state.account.withdraw(amount)

            if "Successful" in result:
                st.success(result)
            else:
                st.error(result)

    else:
        st.warning("⚠ Create an account first")

# ---------------- UPDATE MOBILE ----------------
elif choice == "Update Mobile":

    st.header("📱 Update Mobile Number")

    if st.session_state.account:

        new_mobile = st.text_input("Enter New Mobile Number")

        if st.button("Update"):
            result = st.session_state.account.update_mobile(new_mobile)
            st.success(result)

    else:
        st.warning("⚠ Create an account first")

# ---------------- CHECK BALANCE ----------------
elif choice == "Check Balance":

    st.header("💳 Account Balance")

    if st.session_state.account:
        result = st.session_state.account.check_balance()
        st.success(result)

    else:
        st.warning("⚠ Create an account first")