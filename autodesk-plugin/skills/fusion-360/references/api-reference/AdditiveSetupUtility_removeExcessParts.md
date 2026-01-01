# AdditiveSetupUtility.removeExcessParts Method

Parent Object: [AdditiveSetupUtility](AdditiveSetupUtility.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/ModifyUtility/AdditiveSetupUtility.h>

## Description

Remove components from setups, that are outside of the buildroom.

## Syntax

* [Python](#Python)
* [C++](#C++)

"additiveSetupUtility\_var" is a variable referencing an [AdditiveSetupUtility](AdditiveSetupUtility.htm) object.```` ``` returnValue = additiveSetupUtility_var.removeExcessParts() ``` ```` |

"additiveSetupUtility\_var" is a variable referencing an [AdditiveSetupUtility](AdditiveSetupUtility.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| integer | Returns count of removed parts on success and -1 on failure. |

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |