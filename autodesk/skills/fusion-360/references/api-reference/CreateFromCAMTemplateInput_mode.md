# CreateFromCAMTemplateInput.mode Property

Parent Object: [CreateFromCAMTemplateInput](CreateFromCAMTemplateInput.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CreateFromCAMTemplateInput.h>

## Description

Gets and sets the mode to be used for generation. Defaults to Skip Generation.

## Syntax

* [Python](#Python)
* [C++](#C++)

"createFromCAMTemplateInput\_var" is a variable referencing a CreateFromCAMTemplateInput object. |

"createFromCAMTemplateInput\_var" is a variable referencing a CreateFromCAMTemplateInput object. ```` ``` #include <Cam/CAM/CreateFromCAMTemplateInput.h>  // Get the value of the property. AutomaticGenerationModes propertyValue = createFromCAMTemplateInput_var->mode();  // Set the value of the property, where value_var is an AutomaticGenerationModes. bool returnValue = createFromCAMTemplateInput_var->mode(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an [AutomaticGenerationModes](AutomaticGenerationModes.htm).

## Version

Introduced in version October 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |