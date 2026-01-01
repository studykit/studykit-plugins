# CAMTemplateOperationInput.geometryIndexCount Property![](../images/TestTubeLarge.png)

Parent Object: [CAMTemplateOperationInput](CAMTemplateOperationInput.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::cam" and the header file is <Cam/CAMTemplate/CAMTemplateOperationInput.h>

## Description

Get the number of geometry indices that can be selected.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMTemplateOperationInput\_var" is a variable referencing a CAMTemplateOperationInput object. |

"cAMTemplateOperationInput\_var" is a variable referencing a CAMTemplateOperationInput object. ```` ``` #include <Cam/CAMTemplate/CAMTemplateOperationInput.h>  // Get the value of the property. integer propertyValue = cAMTemplateOperationInput_var->geometryIndexCount(); ``` ```` |

## Property Value

This is a read only property whose value is an integer.

## Version

Introduced in version March 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |