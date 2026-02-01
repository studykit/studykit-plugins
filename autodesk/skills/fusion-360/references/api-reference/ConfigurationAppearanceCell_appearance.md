# ConfigurationAppearanceCell.appearance Property

Parent Object: [ConfigurationAppearanceCell](ConfigurationAppearanceCell.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationAppearanceCell.h>

## Description

Gets and sets the appearance associated with this cell. This property can return null indicating the appearance from the physical material assigned to the object is inherited. Setting the property to null will inherit the appearance from the physical material assigned to the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationAppearanceCell\_var" is a variable referencing a ConfigurationAppearanceCell object. |

"configurationAppearanceCell\_var" is a variable referencing a ConfigurationAppearanceCell object. ```` ``` #include <Fusion/Configurations/ConfigurationAppearanceCell.h>  // Get the value of the property. Ptr<Appearance> propertyValue = configurationAppearanceCell_var->appearance();  // Set the value of the property, where value_var is an Appearance. bool returnValue = configurationAppearanceCell_var->appearance(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an [Appearance](Appearance.htm).

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |