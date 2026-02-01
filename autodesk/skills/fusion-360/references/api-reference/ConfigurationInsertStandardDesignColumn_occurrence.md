# ConfigurationInsertStandardDesignColumn.occurrence Property

Parent Object: [ConfigurationInsertStandardDesignColumn](ConfigurationInsertStandardDesignColumn.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationInsertStandardDesignColumn.h>

## Description

Returns the occurrence being controlled by this column.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationInsertStandardDesignColumn\_var" is a variable referencing a ConfigurationInsertStandardDesignColumn object.  ```` ``` # Get the value of the property. propertyValue = configurationInsertStandardDesignColumn_var.occurrence ``` ```` |

"configurationInsertStandardDesignColumn\_var" is a variable referencing a ConfigurationInsertStandardDesignColumn object. ```` ``` #include <Fusion/Configurations/ConfigurationInsertStandardDesignColumn.h>  // Get the value of the property. Ptr<Occurrence> propertyValue = configurationInsertStandardDesignColumn_var->occurrence(); ``` ```` |

## Property Value

This is a read only property whose value is an [Occurrence](Occurrence.htm).

## Version

Introduced in version September 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |