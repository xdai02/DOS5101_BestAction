"""
    Year 0 original data
"""
YEAR_DATA = {
    "num_of_units_sold": 800000,
    "unit_price": 100,

    "num_of_factories": 1,
    "factory_depreciation": 500000,
    "depreciation_period": 10,

    "num_of_equipment": 0,
    "equipment_depreciation": 200000,
    "raw_materials_inventory_value": 0.1,

    "cogs": 0.3,  # COGS

    "finished_goods_inventory_obsolescence": 0.01,
    "finished_goods_inventory_holding": 1,
    "finished_goods_inventory_holding_cost": 0.1,

    "raw_materials_inventory_obsolescence": 0.01,
    "raw_materials_inventory_holding": 1,
    "raw_materials_inventory_holding_cost": 0.1,

    "logistics_cost": 0.08,

    "rd": 0.05,  # R&D

    "sga": 0.35,  # SG&A
}

"""
    Action list
    Each action contains a collection of value changes and a boolean value indicates whether the effect is delayed.
"""
ACTIONS = [
    # Action 1: Build new factory to increase production capacity
    {
        "num_of_factories": (1, False),  # increase new factory by 1
        "num_of_units_sold": (0.2, True),  # increase by 20% from Year + 1
        "sga": (0.02, False),  # increase by 2%
    },

    # Action 2: Introduce additional new equipment in existing factory to increase capacity for export
    {
        "num_of_equipment": (1, False),  # increase additional equipment by 1
        "num_of_units_sold": (0.02, False),  # increase by 2%
    },

    # Action 3: Introduce new supply sources of wheat to have diversification
    {
        "cogs": (0.02, False),  # increase by 2%
    },

    # Action 4: Create more varieties with localized taste to cater to Southeast Asian markets
    {
        "cogs": (0.12, True),  # increase by 12% from Year + 1
        "finished_goods_inventory_holding": (0.03, False),  # increase by 3%
        "logistics_cost": (0.05, False),  # increase by 5%
    },

    # Action 5: Hold more finished goods to improve product availability for sales
    {
        "num_of_units_sold": (0.07, False),  # increase 7%
        "finished_goods_inventory_holding": (0.04, False),  # increase by 4%
    },

    # Action 6: Setup distribution centres in new countries to be closer to new markets
    {
        "sga": (0.01, False),  # increase by 1%
    },

    # Action 7: Improve product quality and taste hrough R&D
    {
        "unit_price": (0.05, True),  # increase by 5% from Year + 1
        "rd": (0.1, False),  # increase by 10%
    },

    # Action 8: Buy from suppliers with sustainable practices and organic sources
    {
        "cogs": (0.01, False),  # increase by 1%
    },

    # Action 9: Work with its retail customers on risk sharing contracts to carry more of its products
    {
        "num_of_units_sold": (0.1, False),  # increase by 10%
        "raw_materials_inventory_holding": (0.05, False),  # increase by 5%
        "finished_goods_inventory_holding": (0.05, False),  # increase by 5%
    },

    # Action 10: Work with partners to create retail locations offering their noodles and other snacks
    {
        "unit_price": (0.1, False),  # increase by 10% due to broader range of products
        "raw_materials_inventory_holding": (0.05, False),  # increase by 5%
        "finished_goods_inventory_holding": (0.05, False),  # increase by 5%
    },

    # Action 11: Share demand information with suppliers
    {
        "raw_materials_inventory_holding": (-0.2, False),  # reduce by 20%
    },

    # Action 12: Decrease unit sales price
    {
        "unit_price": (-0.05, False),  # decrease 5%
        "num_of_units_sold": (0.1, False),  # increase by 10%
    },

    # Action 13: increase unit sales price
    {
        "unit_price": (0.1, False),  # increase 10%
        "num_of_units_sold": (-0.07, False),  # decrease by 7%
    },

    # Action 14: Invest in worker training
    {
        "cogs": (-0.08, True),  # reduce by 8% from Year + 1
    },

    # Action 15: Grow business through investing in e-commerce
    {
        "num_of_units_sold": (0.1, False),  # increase by 10%
        "logistics_cost": (0.08, False),  # increase by 8%
    },

    # Action 16: Stock up on inventory as safety stock
    {
        "raw_materials_inventory_holding": (0.04, False),  # increase by 4%
        "finished_goods_inventory_holding": (0.04, False),  # increase by 4%
    },
]

"""
    Constrains
"""
CONSTRAINS = [
    (12, 13),  # Action 12 and 13 cannot be taken in the same year
]

"""
    Events
"""
EVENTS = [

]


class ActionAnalyzer:
    def __init__(self, year_data={}, actions=[], constrains=[], events=[]):
        self.__year_data = year_data
        self.__actions = actions
        self.__constrains = constrains
        self.__events = events

    def get_year_data(self):
        """
            Returns current year's data in readable format
        """
        year_data = ""

        year_data += "=" * 50 + "\n"

        year_data += "[Market]\n"
        year_data += "Number of units sold                : %.2f\n" % self.__year_data["num_of_units_sold"]
        year_data += "Unit price                          : %.2f\n" % self.__year_data["unit_price"]
        year_data += "\n"

        year_data += "[Production]\n"
        year_data += "Number of factories                 : %d\n" % self.__year_data["num_of_factories"]
        year_data += "Each factory has depreciation of    : %.2f\n" % self.__year_data["factory_depreciation"]
        year_data += "Depreciation period                 : %.2f\n" % self.__year_data["depreciation_period"]
        year_data += "\n"
        year_data += "Additional new equipment            : %d\n" % self.__year_data["num_of_equipment"]
        year_data += "Additional equipment depreciation   : %.2f\n" % self.__year_data["equipment_depreciation"]
        year_data += "Raw materials inventory value (BOM) : %.2f%%\n" % (
                self.__year_data["raw_materials_inventory_value"] * 100)
        year_data += "\n"

        year_data += "[COGS]                              : %.2f%%\n" % (self.__year_data["cogs"] * 100)
        year_data += "\n"

        year_data += "[Finished goods inventory]\n"
        year_data += "Inventory obsolescence              : %.2f%%\n" % (
                self.__year_data["finished_goods_inventory_obsolescence"] * 100)
        year_data += "Inventory holding                   : %.2f\n" % self.__year_data[
            "finished_goods_inventory_holding"]
        year_data += "Inventory holding cost              : %.2f%%\n" % (
                self.__year_data["finished_goods_inventory_holding_cost"] * 100)
        year_data += "\n"

        year_data += "[Raw materials inventory]\n"
        year_data += "Inventory obsolescence              : %.2f%%\n" % (
                self.__year_data["raw_materials_inventory_obsolescence"] * 100)
        year_data += "Inventory holding                   : %.2f\n" % self.__year_data[
            "raw_materials_inventory_holding"]
        year_data += "Inventory holding cost              : %.2f%%\n" % (
                self.__year_data["raw_materials_inventory_holding_cost"] * 100)
        year_data += "\n"

        year_data += "[Logistics cost]                    : %.2f%%\n" % (self.__year_data["logistics_cost"] * 100)
        year_data += "\n"

        year_data += "[R&D]                               : %.2f%%\n" % (self.__year_data["rd"] * 100)
        year_data += "\n"

        year_data += "[SG&A]                              : %.2f%%\n" % (self.__year_data["sga"] * 100)

        year_data += "=" * 50 + "\n"

        return year_data

    def get_revenue(self):
        """
            Revenue = num_of_units_sold * unit_price
        """
        return self.__year_data["num_of_units_sold"] * self.__year_data["unit_price"]

    def get_cogs(self):
        """
            COGS = Revenue * cogs
        """
        return self.get_revenue() * self.__year_data["cogs"]

    def get_gross_profit(self):
        """
            Gross Profit = Revenue - COGS
        """
        return self.get_revenue() - self.get_cogs()

    def get_rd(self):
        """
            R&D = Revenue * rd
        """
        return self.get_revenue() * self.__year_data["rd"]

    def get_sga(self):
        """
            SG&A = Revenue * sga
        """
        return self.get_revenue() * self.__year_data["sga"]

    def get_logistics(self):
        """
            Logistics = Revenue * logistics_cost
        """
        return self.get_revenue() * self.__year_data["logistics_cost"]

    def get_depreciation(self):
        """
            Depreciation = factory_depreciation + equipment_depreciation
            factory_depreciation = num_of_factories * factory_depreciation
            equipment_depreciation = num_of_equipment * equipment_depreciation
        """
        factory_depreciation = self.__year_data["num_of_factories"] * self.__year_data["factory_depreciation"]
        equipment_depreciation = self.__year_data["num_of_equipment"] * self.__year_data["equipment_depreciation"]
        return factory_depreciation + equipment_depreciation

    def get_fg_inventory(self):
        """
            FG Inventory = Revenue * finished_goods_inventory_holding
        """
        return self.get_revenue() * self.__year_data["finished_goods_inventory_holding"]

    def get_raw_materials_inventory(self):
        """
            Raw Materials Inventory = Revenue * raw_materials_inventory_value
        """
        return self.get_revenue() * self.__year_data["raw_materials_inventory_value"]

    def get_inventory_holding_cost(self):
        """
            Inventory Holding Cost = finished_goods_inventory_holding_cost + raw_materials_inventory_holding_cost
            finished_goods_inventory_holding_cost = FG Inventory * finished_goods_inventory_holding_cost
            raw_materials_inventory_holding_cost = Raw Materials Inventory * raw_materials_inventory_holding_cost
        """
        finished_goods_inventory_holding_cost = self.get_fg_inventory() * self.__year_data[
            "finished_goods_inventory_holding_cost"]
        raw_materials_inventory_holding_cost = self.get_raw_materials_inventory() * self.__year_data[
            "raw_materials_inventory_holding_cost"]
        return finished_goods_inventory_holding_cost + raw_materials_inventory_holding_cost

    def get_inventory_obsolescence(self):
        """
            Inventory Obsolescence = finished_goods_inventory_obsolescence + raw_materials_inventory_obsolescence
            finished_goods_inventory_obsolescence = FG Inventory * finished_goods_inventory_obsolescence
            raw_materials_inventory_obsolescence = Raw Materials Inventory * raw_materials_inventory_obsolescence
        """
        finished_goods_inventory_obsolescence = self.get_fg_inventory() * self.__year_data[
            "finished_goods_inventory_obsolescence"]
        raw_materials_inventory_obsolescence = self.get_raw_materials_inventory() * self.__year_data[
            "raw_materials_inventory_obsolescence"]
        return finished_goods_inventory_obsolescence + raw_materials_inventory_obsolescence

    def get_operating_profit(self):
        """
            Operating Profit = Gross Profit - R&D - SG&A - Logistics - Depreciation - Inventory Holding Cost - Inventory Obsolescence
        """
        return self.get_gross_profit() - self.get_rd() - self.get_sga() - self.get_logistics() - self.get_depreciation() - self.get_inventory_holding_cost() - self.get_inventory_obsolescence()


def main():
    action_analyzer = ActionAnalyzer(YEAR_DATA, ACTIONS, CONSTRAINS, EVENTS)
    year_data = action_analyzer.get_year_data()
    print(year_data)


if __name__ == "__main__":
    main()
