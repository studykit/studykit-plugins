# ConfigurationAppearanceColumn.entity Property

Parent Object: [ConfigurationAppearanceColumn](ConfigurationAppearanceColumn.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationAppearanceColumn.h>

## Description

Returns the Component or BRepBody being controlled by this column. This property returns null when the table being queried was obtained from a DataFile object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationAppearanceColumn\_var" is a variable referencing a ConfigurationAppearanceColumn object. |

"configurationAppearanceColumn\_var" is a variable referencing a ConfigurationAppearanceColumn object. ```` ``` #include <Fusion/Configurations/ConfigurationAppearanceColumn.h>  // Get the value of the property. Ptr<Base> propertyValue = configurationAppearanceColumn_var->entity(); ``` ```` |

## Property Value

This is a read only property whose value is a [Base](Base.htm).

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |