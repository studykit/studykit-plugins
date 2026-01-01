# ShellFeatures.item Method

Parent Object: [ShellFeatures](ShellFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ShellFeatures.h>

## Description

Function that returns the specified shell feature using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"shellFeatures\_var" is a variable referencing a [ShellFeatures](ShellFeatures.htm) object.```` ``` returnValue = shellFeatures_var.item(index) ``` ```` |

"shellFeatures\_var" is a variable referencing a [ShellFeatures](ShellFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ShellFeature](ShellFeature.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |