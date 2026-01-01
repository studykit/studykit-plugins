# Properties.itemByName Method

Parent Object: [Properties](Properties.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Properties.h>

## Description

Returns the specified Property using the name of the property.

## Syntax

* [Python](#Python)
* [C++](#C++)

"properties\_var" is a variable referencing a [Properties](Properties.htm) object.```` ``` returnValue = properties_var.itemByName(name) ``` ```` |

"properties\_var" is a variable referencing a [Properties](Properties.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Property](Property.htm) | Returns the specified property or null if the name doesn't match a property within the collection. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | string | The name of the property to return. This is the name as seen in the user interface. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |