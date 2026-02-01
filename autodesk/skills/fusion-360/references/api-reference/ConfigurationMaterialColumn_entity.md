# ConfigurationMaterialColumn.entity Property

Parent Object: [ConfigurationMaterialColumn](ConfigurationMaterialColumn.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationMaterialColumn.h>

## Description

Returns the Component or BRepBody being modified by this column. This property returns null when the table being queried was obtained from a DataFile object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationMaterialColumn\_var" is a variable referencing a ConfigurationMaterialColumn object. |

"configurationMaterialColumn\_var" is a variable referencing a ConfigurationMaterialColumn object. ```` ``` #include <Fusion/Configurations/ConfigurationMaterialColumn.h>  // Get the value of the property. Ptr<Base> propertyValue = configurationMaterialColumn_var->entity(); ``` ```` |

## Property Value

This is a read only property whose value is a [Base](Base.htm).

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |