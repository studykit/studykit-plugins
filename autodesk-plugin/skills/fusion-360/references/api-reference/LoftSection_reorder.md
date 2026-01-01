# LoftSection.reorder Method

Parent Object: [LoftSection](LoftSection.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/LoftSection.h>

## Description

Repositions this section so that it has the new index specified.

## Syntax

* [Python](#Python)
* [C++](#C++)

"loftSection\_var" is a variable referencing a [LoftSection](LoftSection.htm) object.```` ``` returnValue = loftSection_var.reorder(newIndex) ``` ```` |

"loftSection\_var" is a variable referencing a [LoftSection](LoftSection.htm) object.  ```` ``` #include <Fusion/Features/LoftSection.h>  returnValue = loftSection_var->reorder(newIndex); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the reorder operation was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| newIndex | integer | The new index value. For example, passing in zero as the new index will make this the first section in the loft and (LoftSections.count - 1) will make it the last section. All other sections will be maintain their existing order but be shifted to allow space for this section. |

## Version

Introduced in version August 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |