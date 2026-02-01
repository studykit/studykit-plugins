# TangentDistanceDimConstraintProxy Object

Derived from: [TangentDistanceDimConstraint](../TangentDistanceDimConstraint/TangentDistanceDimConstraint.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../TangentDistanceDimConstraintProxy/TangentDistanceDimConstraintProxy_Delete.md) | Method that deletes the constraint. |
| [GetReferenceKey](../TangentDistanceDimConstraintProxy/TangentDistanceDimConstraintProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AnchorPoints](../TangentDistanceDimConstraintProxy/TangentDistanceDimConstraintProxy_AnchorPoints.md) | Gets the anchor points of dimension. |
| [Application](../TangentDistanceDimConstraintProxy/TangentDistanceDimConstraintProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../TangentDistanceDimConstraintProxy/TangentDistanceDimConstraintProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ContainingOccurrence](../TangentDistanceDimConstraintProxy/TangentDistanceDimConstraintProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [DimensionCenterPoint](../TangentDistanceDimConstraintProxy/TangentDistanceDimConstraintProxy_DimensionCenterPoint.md) | Gets the center of the dimension line. |
| [Driven](../TangentDistanceDimConstraintProxy/TangentDistanceDimConstraintProxy_Driven.md) | Gets and sets whether this dimension constraint is driving the geometry or the geometry is defining the value associated with the constraint. |
| [EntityOne](../TangentDistanceDimConstraintProxy/TangentDistanceDimConstraintProxy_EntityOne.md) | Property that returns the first circle or line being constrained. |
| [EntityTwo](../TangentDistanceDimConstraintProxy/TangentDistanceDimConstraintProxy_EntityTwo.md) | Property that returns the second circle or line being constrained. |
| [LinearDiameter](../TangentDistanceDimConstraintProxy/TangentDistanceDimConstraintProxy_LinearDiameter.md) | Property that returns whether the dimension is a linear diameter style of dimension. Returns True if it is a linear diameter dimension. |
| [NativeObject](../TangentDistanceDimConstraintProxy/TangentDistanceDimConstraintProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [Parameter](../TangentDistanceDimConstraintProxy/TangentDistanceDimConstraintProxy_Parameter.md) | Property that returns the parameter associated with this dimension constraint. If the Driven property of the constraint is True, this will return a ReferenceParameter object. Otherwise it will return a ModelParameter object. |
| [Parent](../TangentDistanceDimConstraintProxy/TangentDistanceDimConstraintProxy_Parent.md) | Property that returns the parent sketch of the object. |
| [ProximityPointOne](../TangentDistanceDimConstraintProxy/TangentDistanceDimConstraintProxy_ProximityPointOne.md) | The point supplied by this argument is used when EntityOne is a circle or arc. This point specifies which of the possible two tangent cases is used when creating the constraint. The closest tangent to the input point is used. If EntityOne is a line, this argument is ignored. |
| [ProximityPointTwo](../TangentDistanceDimConstraintProxy/TangentDistanceDimConstraintProxy_ProximityPointTwo.md) | The point supplied by this argument is used when EntityTwo is a circle or arc. This point specifies which of the possible two tangent cases is used when creating the constraint. The closest tangent to the input point is used. If EntityTwo is a line, this argument is ignored. |
| [TextPoint](../TangentDistanceDimConstraintProxy/TangentDistanceDimConstraintProxy_TextPoint.md) | Gets and sets the position of the dimension text. |
| [Type](../TangentDistanceDimConstraintProxy/TangentDistanceDimConstraintProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Version

Introduced in version 6
