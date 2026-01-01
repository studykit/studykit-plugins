# Properties.item Method

Parent Object: [Properties](Properties.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Properties.h>

## Description

Returns the specified property from the collection using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"properties\_var" is a variable referencing a [Properties](Properties.htm) object.```` ``` returnValue = properties_var.item(index) ``` ```` |

"properties\_var" is a variable referencing a [Properties](Properties.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Property](Property.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | integer | The index of the property within the collection where the first item is 0. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |