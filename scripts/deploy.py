import imp
from brownie import FundMe, network
from scripts.helpful_scripts import get_account

def deploy_fund_me():
    account = get_account()

    if network.show_active() != "development":
        price_feed_address = "0x8A753747A1Fa494EC906cE90E9f37563A8AF630e"
    fund_me = FundMe.deploy(
        '0x8A753747A1Fa494EC906cE90E9f37563A8AF630e',
        {"from":account},
        publish_source=True,
        )


def main():
    deploy_fund_me()