# Attributes.itemByName Method

Parent Object: [Attributes](Attributes.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Attributes.h>

## Description

Returns the specified attribute using the name of the attribute.

## Syntax

* [Python](#Python)
* [C++](#C++)

"attributes\_var" is a variable referencing an [Attributes](Attributes.htm) object.```` ``` returnValue = attributes_var.itemByName(groupName, name) ``` ```` |

"attributes\_var" is a variable referencing an [Attributes](Attributes.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Attribute](Attribute.htm) | Returns the specified attribute or null if no attribute exists with the specified name. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| groupName | string | The name of the attribute group this attribute will belong to. |
| name | string | The name of the attribute. |

## Version

Introduced in version May 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |