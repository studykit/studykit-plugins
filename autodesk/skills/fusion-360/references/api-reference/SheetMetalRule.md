# SheetMetalRule Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/SheetMetalRule.h>

## Description

A sheet metal rule.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](SheetMetalRule_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [deleteMe](SheetMetalRule_deleteMe.htm) | Deletes the rule from the design or library. If the rule is in the library and set as the default rule, you cannot delete it. If the rule is in a design and is used by a component you cannot use it. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [bendRadius](SheetMetalRule_bendRadius.htm) | The interior radius of the bends. Use the returned SheetMetalRuleValue object to get and set the current value of the radius. |
| [gap](SheetMetalRule_gap.htm) | The value used for miter, rip, and seam, gaps. Use the returned SheetMetalRuleValue object to get and set the current value of the gap. |
| [isDefault](SheetMetalRule_isDefault.htm) | This gets and sets which rule in a library is the default rule. This is only valid for rules in a library and will fail for rules in a design. |
| [isUsed](SheetMetalRule_isUsed.htm) | Indicates if this rule is currently being used by a component. This is only valid for rules in a design. |
| [isValid](SheetMetalRule_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [kFactor](SheetMetalRule_kFactor.htm) | The K Factor value that is used when calculating the flat pattern. It must be a value between 0 and 1. |
| [name](SheetMetalRule_name.htm) | The name of the sheet metal rule. When setting the name, it should be unique with respect to other sheet metal rules in the design or library. |
| [objectType](SheetMetalRule_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [parentDesign](SheetMetalRule_parentDesign.htm) | Returns the parent design for a sheet metal rule in a design or it returns null if the sheet metal rule is in the library. |
| [reliefDepth](SheetMetalRule_reliefDepth.htm) | The relief depth used in the flat pattern. Use the returned SheetMetalRuleValue object to get and set the current value of the relief depth. |
| [reliefRemnant](SheetMetalRule_reliefRemnant.htm) | The relief remnant used in the flat pattern. Use the returned SheetMetalRuleValue object to get and set the current value of the relief remnant. |
| [reliefShape](SheetMetalRule_reliefShape.htm) | Gets and sets the bend relief shape to use. |
| [reliefWidth](SheetMetalRule_reliefWidth.htm) | The relief width used in the flat pattern. Use the returned SheetMetalRuleValue object to get and set the current value of the relief width. |
| [thickness](SheetMetalRule_thickness.htm) | The thickness of the part. Use the returned SheetMetalRuleValue object to get and set the current value of the thickness. |
| [threeBendReliefRadius](SheetMetalRule_threeBendReliefRadius.htm) | The relief size used when three bends meet in the flat pattern and the relief shape is "round with radius". Use the returned SheetMetalRuleValue object to get and set the current value of the relief size. |
| [threeBendReliefShape](SheetMetalRule_threeBendReliefShape.htm) | Gets and sets the relief shape to use when three bends intersect. |
| [twoBendReliefPlacement](SheetMetalRule_twoBendReliefPlacement.htm) | Gets and sets the relief placement for a two bend relief shape. When the relief shape is round, both intersection and tangent are valid placements. For square shape, only intersection is valid. For all other shapes, this property will return NoTwoBendReliefPlacement because the placement option is not used. |
| [twoBendReliefShape](SheetMetalRule_twoBendReliefShape.htm) | Gets and sets the relief shape to use when two bends intersect.   When set to square or round relief shape, the value of the twoBendReliefPlacement property will be set to IntersectionTwoBendReliefPlacement. For a round relief shape you can change the twoBendReliefPlacment property to TangentTwoBendReliefPlacement. |
| [twoBendReliefSize](SheetMetalRule_twoBendReliefSize.htm) | The relief size used when two bends meet in the flat pattern and the relief shape is round or square. Use the returned SheetMetalRuleValue object to get and set the current value of the relief size. |
| [units](SheetMetalRule_units.htm) | Gets the units this rule uses to display values in the dialog. Rules currently only use mm or inch and the units are permanently associated with a rule and cannot be modified. |

## Accessed From

[Component.activeSheetMetalRule](Component_activeSheetMetalRule.htm), [ConfigurationSheetMetalRuleCell.sheetMetalRule](ConfigurationSheetMetalRuleCell_sheetMetalRule.htm), [FlatPatternComponent.activeSheetMetalRule](FlatPatternComponent_activeSheetMetalRule.htm), [SheetMetalRules.addByCopy](SheetMetalRules_addByCopy.htm), [SheetMetalRules.item](SheetMetalRules_item.htm), [SheetMetalRules.itemByName](SheetMetalRules_itemByName.htm)

## Version

Introduced in version November 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |