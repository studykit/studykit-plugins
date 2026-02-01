# CAM.checkValidity Method

Parent Object: [CAM](CAM.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAM.h>

## Description

Checks whether the models used by the operations have changed in the mean time and invalidates the affected operations if needed. Should be used for cases where the automatic detection does not work yet, for instance when design changes are expected before a Manufacture API call. Also recommended at the beginning of a script or the beginning of an event handler.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAM\_var" is a variable referencing a [CAM](CAM.htm) object.```` ``` returnValue = cAM_var.checkValidity() ``` ```` |

"cAM\_var" is a variable referencing a [CAM](CAM.htm) object. |

## Version

Introduced in version July 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |