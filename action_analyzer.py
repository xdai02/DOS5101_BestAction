"""
    Actions already happened
"""
ACTIONS_HAPPENED = [
    (4, 11, 13),  # year 1
    # (2, 9, 16),  # year 2
]

"""
    Events already happened
"""
EVENTS_HAPPENED = [
    5,  # year 1
]

"""
    All year data with Year 0 as original
"""
YEAR_DATA = [
    {
        "num_of_units_sold": 800000,
        "unit_price": 100,

        "num_of_factories": 1,
        "factory_depreciation": 500000,
        "depreciation_period": 10,

        "num_of_equipment": 0,
        "equipment_depreciation": 200000,
        "rm_inventory_value": 0.1,

        "cogs": 0.3,  # COGS

        "fg_inventory_obsolescence": 0.01,
        "fg_inventory_holding": 1,
        "fg_inventory_holding_cost": 0.1,

        "rm_inventory_obsolescence": 0.01,
        "rm_inventory_holding": 1,
        "rm_inventory_holding_cost": 0.1,

        "logistics_cost": 0.08,

        "rd": 0.05,  # R&D

        "sga": 0.35,  # SG&A
    },
]

"""
    All actions are allowed to be used at most 3 times
"""
MAX_ACTION_REPEAT = 3

"""
    Action List
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
        "fg_inventory_holding": (0.03, False),  # increase by 3%
        "logistics_cost": (0.05, False),  # increase by 5%
    },

    # Action 5: Hold more finished goods to improve product availability for sales
    {
        "num_of_units_sold": (0.07, False),  # increase 7%
        "fg_inventory_holding": (0.04, False),  # increase by 4%
    },

    # Action 6: Setup distribution centres in new countries to be closer to new markets
    {
        "sga": (0.01, False),  # increase by 1%
    },

    # Action 7: Improve product quality and taste through R&D
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
        "rm_inventory_holding": (0.05, False),  # increase by 5%
        "fg_inventory_holding": (0.05, False),  # increase by 5%
    },

    # Action 10: Work with partners to create retail locations offering their noodles and other snacks
    {
        "unit_price": (0.1, False),  # increase by 10% due to broader range of products
        "rm_inventory_holding": (0.05, False),  # increase by 5%
        "fg_inventory_holding": (0.05, False),  # increase by 5%
    },

    # Action 11: Share demand information with suppliers
    {
        "rm_inventory_holding": (-0.2, False),  # reduce by 20%
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
        "rm_inventory_holding": (0.04, False),  # increase by 4%
        "fg_inventory_holding": (0.04, False),  # increase by 4%
    },
]

"""
    Constrains
"""
CONSTRAINS = [
    (12, 13),  # Action 12 and 13 cannot be taken in the same year
]

"""
    Event List
    Each event contains a collection of actions affected and a boolean value indicates that the effect is taken for the 
    next year.
"""
EVENTS = [
    # Event 1: Demand for instant noodles surge in Asian markets. Those who took Action 2 have a 15% increase in sales.
    # Those that did not take Action 2 have no impact
    {
        "Action_2": {"num_of_units_sold": (0.15, True)}
    },

    # Event 2: A resurgence of new Covid-19 variants causes reduction in retail demand. Those who took Action 10 have a
    # 20% drop in sales. Those that did not take Action 10 have no impact.
    {
        "Action_10": {"num_of_units_sold": (-0.2, True)}
    },

    # Event 3: Customers become more demanding due to competition from the global manufacturers. Those who took Action 7
    # have a 10% increase in sales. Those who did not take Action 7 have a 10% decrease in sales.
    {
        "Action_7": {"num_of_units_sold": (0.1, True)},
        "Action_1": {"num_of_units_sold": (-0.1, True)},
        "Action_2": {"num_of_units_sold": (-0.1, True)},
        "Action_3": {"num_of_units_sold": (-0.1, True)},
        "Action_4": {"num_of_units_sold": (-0.1, True)},
        "Action_5": {"num_of_units_sold": (-0.1, True)},
        "Action_6": {"num_of_units_sold": (-0.1, True)},
        "Action_8": {"num_of_units_sold": (-0.1, True)},
        "Action_9": {"num_of_units_sold": (-0.1, True)},
        "Action_10": {"num_of_units_sold": (-0.1, True)},
        "Action_11": {"num_of_units_sold": (-0.1, True)},
        "Action_12": {"num_of_units_sold": (-0.1, True)},
        "Action_13": {"num_of_units_sold": (-0.1, True)},
        "Action_14": {"num_of_units_sold": (-0.1, True)},
        "Action_15": {"num_of_units_sold": (-0.1, True)},
        "Action_16": {"num_of_units_sold": (-0.1, True)},
    },

    # Event 4: Export restrictions on wheat are imposed in major producing countries due to global shortage. Those who
    # took action 3 are not affected.  Those who did not take action 3 have a 5% increase in COGS due to higher 
    # purchasing costs
    {
        "Action_1": {"cogs": (0.05, True)},
        "Action_2": {"cogs": (0.05, True)},
        "Action_4": {"cogs": (0.05, True)},
        "Action_5": {"cogs": (0.05, True)},
        "Action_6": {"cogs": (0.05, True)},
        "Action_7": {"cogs": (0.05, True)},
        "Action_8": {"cogs": (0.05, True)},
        "Action_9": {"cogs": (0.05, True)},
        "Action_10": {"cogs": (0.05, True)},
        "Action_11": {"cogs": (0.05, True)},
        "Action_12": {"cogs": (0.05, True)},
        "Action_13": {"cogs": (0.05, True)},
        "Action_14": {"cogs": (0.05, True)},
        "Action_15": {"cogs": (0.05, True)},
        "Action_16": {"cogs": (0.05, True)},
    },

    # Event 5: Shipping costs skyrocket.  Those who took action 6 have no impact. Those who did not take action 6 have
    # their logistics costs increase by 10%
    {
        "Action_1": {"logistics_cost": (0.1, True)},
        "Action_2": {"logistics_cost": (0.1, True)},
        "Action_3": {"logistics_cost": (0.1, True)},
        "Action_4": {"logistics_cost": (0.1, True)},
        "Action_5": {"logistics_cost": (0.1, True)},
        "Action_7": {"logistics_cost": (0.1, True)},
        "Action_8": {"logistics_cost": (0.1, True)},
        "Action_9": {"logistics_cost": (0.1, True)},
        "Action_10": {"logistics_cost": (0.1, True)},
        "Action_11": {"logistics_cost": (0.1, True)},
        "Action_12": {"logistics_cost": (0.1, True)},
        "Action_13": {"logistics_cost": (0.1, True)},
        "Action_14": {"logistics_cost": (0.1, True)},
        "Action_15": {"logistics_cost": (0.1, True)},
        "Action_16": {"logistics_cost": (0.1, True)},
    },

    # Event 6: There is an increase in consumer awareness for sustainable sourcing practices.  Those who took Action 8
    # have an increase in sales by 20%. Those who did not take action 8 have no impact
    {
        "Action_8": {"num_of_units_sold": (0.2, True)},
    },

    # Event 7: A heatwave causes electricity outage. Those who took Action 16 have no impact. Those who did not take
    # Action 16 have a 20% drop in sales
    {
        "Action_1": {"num_of_units_sold": (-0.2, True)},
        "Action_2": {"num_of_units_sold": (-0.2, True)},
        "Action_3": {"num_of_units_sold": (-0.2, True)},
        "Action_4": {"num_of_units_sold": (-0.2, True)},
        "Action_5": {"num_of_units_sold": (-0.2, True)},
        "Action_6": {"num_of_units_sold": (-0.2, True)},
        "Action_7": {"num_of_units_sold": (-0.2, True)},
        "Action_8": {"num_of_units_sold": (-0.2, True)},
        "Action_9": {"num_of_units_sold": (-0.2, True)},
        "Action_10": {"num_of_units_sold": (-0.2, True)},
        "Action_11": {"num_of_units_sold": (-0.2, True)},
        "Action_12": {"num_of_units_sold": (-0.2, True)},
        "Action_13": {"num_of_units_sold": (-0.2, True)},
        "Action_14": {"num_of_units_sold": (-0.2, True)},
        "Action_15": {"num_of_units_sold": (-0.2, True)},
    },
]


def dict_add(dictionary, key, value, default_value=0):
    """
        Add a kv-pair to the dictionary with default_value if not exist
    """
    if key not in dictionary:
        dictionary[key] = default_value
    dictionary[key] += value


class ActionAnalyzer:
    def __init__(self, year_data, actions, max_action_repeat, constrains, events, actions_happened, events_happened):
        """
            Set up date set
            :param year_data: init year data
            :param actions: action set
            :param max_action_repeat: limit usage for each action
            :param constrains: constrained actions
            :param events: event set
            :param actions_happened: actions already happened
            :param events_happened: events already happened
        """
        self.__year_data = year_data
        self.__actions = actions
        self.__action_counter = [max_action_repeat] * len(actions)
        self.__constrains = constrains
        self.__events = events
        self.__actions_happened = actions_happened
        self.__events_happened = events_happened

        self.__delayed_effects = {}  # store the effects happened in Year + 1

    def get_year_data(self, year_num=-1):
        """
            Returns Year X's data in readable format
        """
        year_data = self.__year_data[year_num]

        year_data_str = ""
        year_data_str += "=" * 50 + "\n"

        year_data_str += "[Market]\n"
        year_data_str += "Number of units sold                : %.2f\n" % year_data["num_of_units_sold"]
        year_data_str += 'Unit price                          : %.2f\n' % year_data["unit_price"]
        year_data_str += "\n"

        year_data_str += "[Production]\n"
        year_data_str += "Number of factories               : %d\n" % year_data["num_of_factories"]
        year_data_str += "Each factory has depreciation of  : %.2f\n" % year_data["factory_depreciation"]
        year_data_str += "Depreciation period               : %.2f\n" % year_data["depreciation_period"]
        year_data_str += "\n"
        year_data_str += "Additional new equipment          : %d\n" % year_data["num_of_equipment"]
        year_data_str += "Additional equipment depreciation : %.2f\n" % year_data["equipment_depreciation"]
        year_data_str += "Raw materials inventory value     : %.2f%%\n" % (year_data["rm_inventory_value"] * 100)
        year_data_str += "\n"

        year_data_str += "[COGS]                            : %.2f%%\n" % (year_data["cogs"] * 100)
        year_data_str += "\n"

        year_data_str += "[Finished goods inventory]\n"
        year_data_str += "Inventory obsolescence            : %.2f%%\n" % (year_data["fg_inventory_obsolescence"] * 100)
        year_data_str += "Inventory holding                 : %.2f\n" % year_data["fg_inventory_holding"]
        year_data_str += "Inventory holding cost            : %.2f%%\n" % (year_data["fg_inventory_holding_cost"] * 100)
        year_data_str += "\n"

        year_data_str += "[Raw materials inventory]\n"
        year_data_str += "Inventory obsolescence            : %.2f%%\n" % (year_data["rm_inventory_obsolescence"] * 100)
        year_data_str += "Inventory holding                 : %.2f\n" % year_data["rm_inventory_holding"]
        year_data_str += "Inventory holding cost            : %.2f%%\n" % (year_data["rm_inventory_holding_cost"] * 100)
        year_data_str += "\n"

        year_data_str += "[Logistics cost]                  : %.2f%%\n" % (year_data["logistics_cost"] * 100)
        year_data_str += "\n"

        year_data_str += "[R&D]                             : %.2f%%\n" % (year_data["rd"] * 100)
        year_data_str += "\n"

        year_data_str += "[SG&A]                            : %.2f%%\n" % (year_data["sga"] * 100)

        year_data_str += "=" * 50 + "\n"

        return year_data_str

    def get_revenue(self, year_num=-1):
        """
            Revenue = num_of_units_sold * unit_price
        """
        year_data = self.__year_data[year_num]
        return year_data["num_of_units_sold"] * year_data["unit_price"]

    def get_cogs(self, year_num=-1):
        """
            COGS = Revenue * cogs
        """
        year_data = self.__year_data[year_num]
        return self.get_revenue(year_num) * year_data["cogs"]

    def get_gross_profit(self, year_num=-1):
        """
            Gross Profit = Revenue - COGS
        """
        return self.get_revenue(year_num) - self.get_cogs(year_num)

    def get_rd(self, year_num=-1):
        """
            R&D = Revenue * rd
        """
        year_data = self.__year_data[year_num]
        return self.get_revenue(year_num) * year_data["rd"]

    def get_sga(self, year_num=-1):
        """
            SG&A = Revenue * sga
        """
        year_data = self.__year_data[year_num]
        return self.get_revenue(year_num) * year_data["sga"]

    def get_logistics(self, year_num=-1):
        """
            Logistics = Revenue * logistics_cost
        """
        year_data = self.__year_data[year_num]
        return self.get_revenue(year_num) * year_data["logistics_cost"]

    def get_depreciation(self, year_num=-1):
        """
            Depreciation = factory_depreciation + equipment_depreciation
            factory_depreciation = num_of_factories * factory_depreciation
            equipment_depreciation = num_of_equipment * equipment_depreciation
        """
        year_data = self.__year_data[year_num]
        factory_depreciation = year_data["num_of_factories"] * year_data["factory_depreciation"]
        equipment_depreciation = year_data["num_of_equipment"] * year_data["equipment_depreciation"]
        return factory_depreciation + equipment_depreciation

    def get_fg_inventory(self, year_num=-1):
        """
            FG Inventory = Revenue * fg_inventory_holding
        """
        year_data = self.__year_data[year_num]
        return self.get_revenue(year_num) * year_data["fg_inventory_holding"]

    def get_raw_materials_inventory(self, year_num=-1):
        """
            Raw Materials Inventory = Revenue * rm_inventory_value
        """
        year_data = self.__year_data[year_num]
        return self.get_revenue(year_num) * year_data["rm_inventory_value"]

    def get_inventory_holding_cost(self, year_num=-1):
        """
            Inventory Holding Cost = fg_inventory_holding_cost + rm_inventory_holding_cost
            fg_inventory_holding_cost = FG Inventory * fg_inventory_holding_cost
            rm_inventory_holding_cost = Raw Materials Inventory * rm_inventory_holding_cost
        """
        year_data = self.__year_data[year_num]
        fg_inventory_holding_cost = self.get_fg_inventory(year_num) * year_data["fg_inventory_holding_cost"]
        rm_inventory_holding_cost = self.get_raw_materials_inventory(year_num) * year_data["rm_inventory_holding_cost"]
        return fg_inventory_holding_cost + rm_inventory_holding_cost

    def get_inventory_obsolescence(self, year_num=-1):
        """
            Inventory Obsolescence = fg_inventory_obsolescence + rm_inventory_obsolescence
            fg_inventory_obsolescence = FG Inventory * fg_inventory_obsolescence
            rm_inventory_obsolescence = Raw Materials Inventory * rm_inventory_obsolescence
        """
        year_data = self.__year_data[year_num]
        fg_inventory_obsolescence = self.get_fg_inventory(year_num) * year_data["fg_inventory_obsolescence"]
        rm_inventory_obsolescence = self.get_raw_materials_inventory(year_num) * year_data["rm_inventory_obsolescence"]
        return fg_inventory_obsolescence + rm_inventory_obsolescence

    def get_operating_profit(self, year_num=-1):
        """
            Operating Profit = Gross Profit - R&D - SG&A
                                - Logistics - Depreciation
                                - Inventory Holding Cost - Inventory Obsolescence
        """
        return self.get_gross_profit(year_num) - self.get_rd(year_num) - self.get_sga(year_num) \
               - self.get_logistics(year_num) - self.get_depreciation(year_num) \
               - self.get_inventory_holding_cost(year_num) - self.get_inventory_obsolescence(year_num)

    def analyze(self):
        """
            Analyze actions for next year
        """
        self.__update_data()

    def __update_data(self):
        """
            Update data based on the actions already taken
        """
        for action in self.__actions_happened:
            self.take_action(action)

    def take_action(self, actions):
        """
            Take given actions
            :param actions: a tuple of actions
        """
        # add delayed effects to current effects
        action_effects = self.__delayed_effects.copy()
        self.__delayed_effects.clear()

        # get all the effects for each action
        for action in actions:
            action_index = action - 1
            action_item = self.__actions[action_index]
            self.__action_counter[action_index] -= 1

            for item_name, item_value in action_item.items():
                item_changed_rate, is_delayed = item_value

                # if this action effect in Year + 1
                if is_delayed:
                    dict_add(self.__delayed_effects, item_name, item_changed_rate)
                else:
                    dict_add(action_effects, item_name, item_changed_rate)

        current_year_data = self.__year_data[-1].copy()
        self.__year_data.append(current_year_data)

        for effect_name, effect_rate in action_effects.items():
            # number of factories/equipment are increased/decreased by an integer
            if effect_name == "num_of_factories" or effect_name == "num_of_equipment":
                current_year_data[effect_name] += effect_rate
            # others are increased/decreased by a percentage
            else:
                current_year_data[effect_name] *= (1 + effect_rate)


def main():
    # set up data set
    action_analyzer = ActionAnalyzer(
        YEAR_DATA, ACTIONS, MAX_ACTION_REPEAT, CONSTRAINS, EVENTS, ACTIONS_HAPPENED, EVENTS_HAPPENED
    )

    # start analyzing
    action_analyzer.analyze()

    # print result
    year_data = action_analyzer.get_year_data(1)
    print(year_data)


if __name__ == "__main__":
    main()
