# ConfigurationInsertStandardDesignColumn.title Property

Parent Object: [ConfigurationInsertStandardDesignColumn](ConfigurationInsertStandardDesignColumn.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationInsertStandardDesignColumn.h>

## Description

The title of this column. In a top table, this can only be edited for suppression, visibility, parameter, and theme table columns. It behaves as read-only for all other types. In a theme table, the title of all the columns can be modified except for the column that represents the root component for materials and appearances.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationInsertStandardDesignColumn\_var" is a variable referencing a ConfigurationInsertStandardDesignColumn object.  ```` ``` # Get the value of the property. propertyValue = configurationInsertStandardDesignColumn_var.title  # Set the value of the property. configurationInsertStandardDesignColumn_var.title = propertyValue ``` ```` |

"configurationInsertStandardDesignColumn\_var" is a variable referencing a ConfigurationInsertStandardDesignColumn object. ```` ``` #include <Fusion/Configurations/ConfigurationInsertStandardDesignColumn.h>  // Get the value of the property. string propertyValue = configurationInsertStandardDesignColumn_var->title();  // Set the value of the property, where value_var is a string. bool returnValue = configurationInsertStandardDesignColumn_var->title(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version September 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |