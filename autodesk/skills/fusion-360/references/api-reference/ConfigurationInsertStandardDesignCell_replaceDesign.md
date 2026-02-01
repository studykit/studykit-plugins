# ConfigurationInsertStandardDesignCell.replaceDesign Property

Parent Object: [ConfigurationInsertStandardDesignCell](ConfigurationInsertStandardDesignCell.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationInsertStandardDesignCell.h>

## Description

Gets and sets which ConfigurationReplaceDesign object will be used when the row this cell is in is active. When setting this property, only ConfigurationReplaceDesign objects defined for the parent column of this cell can be used.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationInsertStandardDesignCell\_var" is a variable referencing a ConfigurationInsertStandardDesignCell object. |

"configurationInsertStandardDesignCell\_var" is a variable referencing a ConfigurationInsertStandardDesignCell object. ```` ``` #include <Fusion/Configurations/ConfigurationInsertStandardDesignCell.h>  // Get the value of the property. Ptr<ConfigurationReplaceDesign> propertyValue = configurationInsertStandardDesignCell_var->replaceDesign();  // Set the value of the property, where value_var is a ConfigurationReplaceDesign. bool returnValue = configurationInsertStandardDesignCell_var->replaceDesign(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [ConfigurationReplaceDesign](ConfigurationReplaceDesign.htm).

## Version

Introduced in version September 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |