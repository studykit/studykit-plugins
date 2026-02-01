# LoftCenterLineOrRails.item Method

Parent Object: [LoftCenterLineOrRails](LoftCenterLineOrRails.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/LoftCenterLineOrRails.h>

## Description

Function that returns the specified LoftCenterLineOrRail using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"loftCenterLineOrRails\_var" is a variable referencing a [LoftCenterLineOrRails](LoftCenterLineOrRails.htm) object.```` ``` returnValue = loftCenterLineOrRails_var.item(index) ``` ```` |

"loftCenterLineOrRails\_var" is a variable referencing a [LoftCenterLineOrRails](LoftCenterLineOrRails.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [LoftCenterLineOrRail](LoftCenterLineOrRail.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | integer | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version August 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |