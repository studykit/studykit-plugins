# PlasticRule Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Plastic/PlasticRule.h>

## Description

A plastic rule.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](PlasticRule_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [deleteMe](PlasticRule_deleteMe.htm) | Deletes the rule from the design or library. If the rule is in the library and set as the default rule, you cannot delete it. If the rule is in a design and is used by a component you cannot delete it. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [clearance](PlasticRule_clearance.htm) | The clearance used for plastic features. When using a float to set the value, it is defined in centimeters. When using a string to set the expression, the units can be defined as part of the expression or it defaults to the units associated with the rule if no units are specified. |
| [draftAngle](PlasticRule_draftAngle.htm) | The draft angle used for plastic features. When using a float to set the value, it is defined in radians. When using a string to set the expression it uses degrees. |
| [isDefault](PlasticRule_isDefault.htm) | This gets and sets which rule in a library is the default rule. This is only valid for rules in a library and will fail for rules in a design. |
| [isUsed](PlasticRule_isUsed.htm) | Indicates if this rule is currently being used by a component. This is only valid for rules in a design. |
| [isValid](PlasticRule_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [knifeEdgeThreshold](PlasticRule_knifeEdgeThreshold.htm) | The minimal thickness where an edge is considered a knife edge. This is used by the Design Advice command when analyzing the part for manufacturability. |
| [material](PlasticRule_material.htm) | Gets and sets the material assigned to this plastic rule |
| [maximumThickness](PlasticRule_maximumThickness.htm) | The maximum thickness of the part in centimeters. This is used by the Design Advice command when analyzing the part for manufacturability. |
| [minimumDraftAngle](PlasticRule_minimumDraftAngle.htm) | The minimum draft angle allowed in radians. This is used by the Design Advice command when analyzing the part for manufacturability. |
| [minimumThickness](PlasticRule_minimumThickness.htm) | The minimum thickness of the part in centimeters. This is used by the Design Advice command when analyzing the part for manufacturability. |
| [name](PlasticRule_name.htm) | The name of the plastic rule. When setting the name, it must be unique with respect to other plastic rules in the design or library. |
| [nominalRadius](PlasticRule_nominalRadius.htm) | The nominal radius used for plastic features. When using a float to set the value, it is defined in centimeters. When using a string to set the expression, the units can be defined as part of the expression or it defaults to the units associated with the rule if no units are specified. |
| [objectType](PlasticRule_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |
| [parentDesign](PlasticRule_parentDesign.htm) | Returns the parent design for a plastic rule in a design or it returns null if the plastic rule is in the library. |
| [revealHeight](PlasticRule_revealHeight.htm) | The reveal height used for plastic features. When using a float to set the value, it is defined in centimeters. When using a string to set the expression, the units can be defined as part of the expression or it defaults to the units associated with the rule if no units are specified. |
| [thickness](PlasticRule_thickness.htm) | The thickness used for plastic features. This value must be within the range specified by the minimumThickness and maximumThickness properties. This is used by the plastic commands when a wall thickness is needed.   When using a float to set the value, it is defined in centimeters. When using a string to set the expression, the units can be defined as part of the expression or it defaults to the units associated with the rule if no units are specified. |
| [thicknessVariation](PlasticRule_thicknessVariation.htm) | The maximum thickness of the part. This is used by the Design Advice command when analyzing the part for manufacturability.   When using a float to set the value, it is defined in centimeters. When using a string to set the expression, the units can be defined as part of the expression or it defaults to the units associated with the rule if no units are specified. |
| [units](PlasticRule_units.htm) | Gets the units this rule uses to display values in the dialog. Rules currently only use mm or inch and the units are permanently associated with a rule and cannot be modified. |

## Accessed From

[ConfigurationPlasticRuleCell.plasticRule](ConfigurationPlasticRuleCell_plasticRule.htm), [PlasticRules.addByCopy](PlasticRules_addByCopy.htm), [PlasticRules.item](PlasticRules_item.htm), [PlasticRules.itemByName](PlasticRules_itemByName.htm)

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |