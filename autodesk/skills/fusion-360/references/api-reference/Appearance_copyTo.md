# Appearance.copyTo Method

Parent Object: [Appearance](Appearance.htm)
Defined in namespace "adsk::core" and the header file is <Core/Materials/Appearance.h>

## Description

This function is retired. See more information in the 'Remarks' section below.

## Remarks

This method has been retired and replaced by the addByCopyMethod on the Appearances object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"appearance\_var" is a variable referencing an [Appearance](Appearance.htm) object.```` ``` returnValue = appearance_var.copyTo(target) ``` ```` |

"appearance\_var" is a variable referencing an [Appearance](Appearance.htm) object.  ```` ``` #include <Core/Materials/Appearance.h>  returnValue = appearance_var->copyTo(target); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the copy was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| target | [Base](Base.htm) | The target can be a Design or FavoriteAppearances object. |

## Version

Introduced in version August 2014
Retired in version July 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |