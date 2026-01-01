# ConfigurationInsertStandardDesignColumn.replaceDesigns Property

Parent Object: [ConfigurationInsertStandardDesignColumn](ConfigurationInsertStandardDesignColumn.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationInsertStandardDesignColumn.h>

## Description

Provides access to the list of replace designs that have been defined for this column. Using the returned collection you can define new ConfigurationReplaceDesign objects. Use the cells in the column to specify which one of the defined replace designs is used for a specific row.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationInsertStandardDesignColumn\_var" is a variable referencing a ConfigurationInsertStandardDesignColumn object. |

"configurationInsertStandardDesignColumn\_var" is a variable referencing a ConfigurationInsertStandardDesignColumn object. ```` ``` #include <Fusion/Configurations/ConfigurationInsertStandardDesignColumn.h>  // Get the value of the property. Ptr<ConfigurationReplaceDesigns> propertyValue = configurationInsertStandardDesignColumn_var->replaceDesigns(); ``` ```` |

## Property Value

This is a read only property whose value is a [ConfigurationReplaceDesigns](ConfigurationReplaceDesigns.htm).

## Version

Introduced in version September 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |