# AdditiveSetupUtility.splitSupport Method

Parent Object: [AdditiveSetupUtility](AdditiveSetupUtility.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/ModifyUtility/AdditiveSetupUtility.h>

## Description

Splits support structure of given target bodies into separate mesh body.

## Syntax

* [Python](#Python)
* [C++](#C++)

"additiveSetupUtility\_var" is a variable referencing an [AdditiveSetupUtility](AdditiveSetupUtility.htm) object.```` ``` returnValue = additiveSetupUtility_var.splitSupport(targets, splitType) ``` ```` |

"additiveSetupUtility\_var" is a variable referencing an [AdditiveSetupUtility](AdditiveSetupUtility.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | True on success, false on errors |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| targets | Base[] | Targets contain any input bodies whose support is to be inserted into a new mesh body. Input target must belong to the setup and must be part of the associated manufacturing model. Raises an error if any input target is not part of the setup or is not part of the associated manufacturing model. |
| splitType | [SplitSupportTypes](SplitSupportTypes.htm) | The splitType defines the behavior for support that contains solid and open mesh geometry. |

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |