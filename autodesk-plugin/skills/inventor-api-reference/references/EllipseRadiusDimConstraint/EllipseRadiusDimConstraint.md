# EllipseRadiusDimConstraint Object

Derived from: [DimensionConstraint](../DimensionConstraint/DimensionConstraint.md) Object

## Description

The EllipseRadiusDimConstraint object represents a constraint that controls either the major or minor radius of an ellipse.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../EllipseRadiusDimConstraint/EllipseRadiusDimConstraint_Delete.md) | Method that deletes the constraint. |
| [GetReferenceKey](../EllipseRadiusDimConstraint/EllipseRadiusDimConstraint_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AnchorPoints](../EllipseRadiusDimConstraint/EllipseRadiusDimConstraint_AnchorPoints.md) | Gets the anchor points of dimension. |
| [Application](../EllipseRadiusDimConstraint/EllipseRadiusDimConstraint_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../EllipseRadiusDimConstraint/EllipseRadiusDimConstraint_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [DimensionCenterPoint](../EllipseRadiusDimConstraint/EllipseRadiusDimConstraint_DimensionCenterPoint.md) | Gets the center of the dimension line. |
| [Driven](../EllipseRadiusDimConstraint/EllipseRadiusDimConstraint_Driven.md) | Gets and sets whether this dimension constraint is driving the geometry or the geometry is defining the value associated with the constraint. |
| [Entity](../EllipseRadiusDimConstraint/EllipseRadiusDimConstraint_Entity.md) | Property that returns the ellipse or elliptical arc being constrained. |
| [MajorRadius](../EllipseRadiusDimConstraint/EllipseRadiusDimConstraint_MajorRadius.md) | Property that returns whether the proxy constraint is controlling the major or minor radius of the ellipse. Returns true if it is the major radius. |
| [Parameter](../EllipseRadiusDimConstraint/EllipseRadiusDimConstraint_Parameter.md) | Property that returns the parameter associated with this dimension constraint. If the Driven property of the constraint is True, this will return a ReferenceParameter object. Otherwise it will return a ModelParameter object. |
| [Parent](../EllipseRadiusDimConstraint/EllipseRadiusDimConstraint_Parent.md) | Property that returns the parent sketch of the object. |
| [TextPoint](../EllipseRadiusDimConstraint/EllipseRadiusDimConstraint_TextPoint.md) | Gets and sets the position of the dimension text. |
| [Type](../EllipseRadiusDimConstraint/EllipseRadiusDimConstraint_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[DimensionConstraints.AddEllipseRadius](../DimensionConstraints/DimensionConstraints_AddEllipseRadius.md), [EllipseRadiusDimConstraintProxy.NativeObject](../EllipseRadiusDimConstraintProxy/EllipseRadiusDimConstraintProxy_NativeObject.md)

## Derived Classes

[EllipseRadiusDimConstraintProxy](../EllipseRadiusDimConstraintProxy/EllipseRadiusDimConstraintProxy.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create sketch elliptical arc](../../sample-programs/SketchEllipticalArc_Sample.md) | This sample demonstrates creating an elliptical arc in a sketch and dimensioning its minor radius. |

## Version

Introduced in version 5
