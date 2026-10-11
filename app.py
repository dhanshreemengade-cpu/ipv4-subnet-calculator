
import streamlit as st
import ipaddress

st.set_page_config(
    page_title="IPv4 Subnet Calculator",
    page_icon="🌐"
)

st.title("🌐 IPv4 Subnet Calculator")
st.write("Calculate IPv4 subnet details easily.")

ip_address = st.text_input(
    "Enter IPv4 Address",
    placeholder="192.168.1.10"
)

subnet_input = st.text_input(
    "Enter Subnet Mask or CIDR Prefix",
    placeholder="255.255.255.0 or 24"
)

if st.button("Calculate Subnet"):
    try:
        ip = ipaddress.IPv4Address(ip_address.strip())
        mask = subnet_input.strip()

        if mask.isdigit():
            prefix = int(mask)

            if not 0 <= prefix <= 32:
                raise ValueError("CIDR must be between 0 and 32")

            network = ipaddress.IPv4Network(
                f"{ip}/{prefix}", strict=False
            )
        else:
            network = ipaddress.IPv4Network(
                f"{ip}/{mask}", strict=False
            )

        total = network.num_addresses
        prefix_length = network.prefixlen

        if prefix_length == 32:
            usable = 1
            first_ip = network.network_address
            last_ip = network.broadcast_address
        elif prefix_length == 31:
            usable = 2
            first_ip = network.network_address
            last_ip = network.broadcast_address
        else:
            usable = max(0, total - 2)
            first_ip = network.network_address + 1
            last_ip = network.broadcast_address - 1

        st.success("Calculation completed!")

        st.subheader("Subnet Details")
        st.write("IP Address:", ip)
        st.write("Network Address:", network.network_address)
        st.write("Subnet Mask:", network.netmask)
        st.write("CIDR Prefix:", f"/{prefix_length}")
        st.write("Broadcast Address:", network.broadcast_address)
        st.write("First Usable IP:", first_ip)
        st.write("Last Usable IP:", last_ip)
        st.write("Total IP Addresses:", total)
        st.write("Usable Host Addresses:", usable)
        st.write("Wildcard Mask:", network.hostmask)

    except ValueError:
        st.error(
            "Invalid IP address or subnet mask. "
            "Please check your input."
        )

st.divider()
st.caption("ACN Microproject | Diploma Computer Engineering")
