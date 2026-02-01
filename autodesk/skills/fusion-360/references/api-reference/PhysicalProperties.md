# PhysicalProperties Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/PhysicalProperties.h>

## Description

The physical properties of a Component, Occurrence or BRepBody

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](PhysicalProperties_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [getPrincipalAxes](PhysicalProperties_getPrincipalAxes.htm) | Method that returns the principal axes. |
| [getPrincipalMomentsOfInertia](PhysicalProperties_getPrincipalMomentsOfInertia.htm) | Method that returns the moments of inertia about the principal axes. Unit for returned values is kg\*cm^2. |
| [getRadiusOfGyration](PhysicalProperties_getRadiusOfGyration.htm) | Method that returns the radius of gyration about the principal axes. Unit for returned values is cm. |
| [getRotationToPrincipal](PhysicalProperties_getRotationToPrincipal.htm) | Gets the rotation from the world coordinate system of the target to the principal coordinate system. |
| [getXYZMomentsOfInertia](PhysicalProperties_getXYZMomentsOfInertia.htm) | Method that gets the moment of inertia about the world coordinate system. Unit for returned values is kg\*cm^2. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [accuracy](PhysicalProperties_accuracy.htm) | Returns the accuracy that was used for the calculation. |
| [area](PhysicalProperties_area.htm) | Gets the area in square centimeters. |
| [centerOfMass](PhysicalProperties_centerOfMass.htm) | Returns the center of mass position |
| [density](PhysicalProperties_density.htm) | Gets the density in kilograms per cubic centimeter. |
| [isValid](PhysicalProperties_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [mass](PhysicalProperties_mass.htm) | Gets the mass in kilograms. |
| [objectType](PhysicalProperties_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [volume](PhysicalProperties_volume.htm) | Gets the volume in the cubic centimeters. |

## Accessed From

[BRepBody.getPhysicalProperties](BRepBody_getPhysicalProperties.htm), [BRepBody.physicalProperties](BRepBody_physicalProperties.htm), [Component.getPhysicalProperties](Component_getPhysicalProperties.htm), [Component.physicalProperties](Component_physicalProperties.htm), [Design.physicalProperties](Design_physicalProperties.htm), [FlatPatternComponent.getPhysicalProperties](FlatPatternComponent_getPhysicalProperties.htm), [FlatPatternComponent.physicalProperties](FlatPatternComponent_physicalProperties.htm), [FlatPatternProduct.physicalProperties](FlatPatternProduct_physicalProperties.htm), [Occurrence.getPhysicalProperties](Occurrence_getPhysicalProperties.htm), [Occurrence.physicalProperties](Occurrence_physicalProperties.htm), [WorkingModel.physicalProperties](WorkingModel_physicalProperties.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Get Physical Properties API Sample](GetPhysicalProperties_Sample.htm) | Script that demonstrates getting physical properties using the API. When this script is run it will create a new document, build a simple model, and get the various physical properties from the model. |

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |