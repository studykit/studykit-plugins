# PropertyGroup.itemByName Method

Parent Object: [PropertyGroup](PropertyGroup.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/PropertyGroup.h>

## Description

Returns the specified Property using the name of the property.

## Syntax

* [Python](#Python)
* [C++](#C++)

"propertyGroup\_var" is a variable referencing a [PropertyGroup](PropertyGroup.htm) object.```` ``` returnValue = propertyGroup_var.itemByName(name) ``` ```` |

"propertyGroup\_var" is a variable referencing a [PropertyGroup](PropertyGroup.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Property](Property.htm) | Returns the specified property or null if the name doesn't match a property within the group. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | string | The name of the property to return. This is the name as seen in the user interface and may be localized. |

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |