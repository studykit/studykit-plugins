# ShellFeature.setThicknesses Method

Parent Object: [ShellFeature](ShellFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ShellFeature.h>

## Description

Method that sets the inside and outside thicknesses of the shell.

## Syntax

* [Python](#Python)
* [C++](#C++)

"shellFeature\_var" is a variable referencing a [ShellFeature](ShellFeature.htm) object.```` ``` returnValue = shellFeature_var.setThicknesses(insideThickness, outsideThickness) ``` ```` |

"shellFeature\_var" is a variable referencing a [ShellFeature](ShellFeature.htm) object.  ```` ``` #include <Fusion/Features/ShellFeature.h>  returnValue = shellFeature_var->setThicknesses(insideThickness, outsideThickness); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if successful |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| insideThickness | [ValueInput](ValueInput.htm) | ValueInput object that defines the inside thickness. If set to null, the inside thickness is removed. |
| outsideThickness | [ValueInput](ValueInput.htm) | ValueInput object that defines the outside thickness. If set to null, the outside thickness is removed. |

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |