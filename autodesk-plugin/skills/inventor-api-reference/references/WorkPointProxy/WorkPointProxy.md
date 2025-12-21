# WorkPointProxy Object

Derived from: [WorkPoint](../WorkPoint/WorkPoint.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../WorkPointProxy/WorkPointProxy_Delete.md) | Method that deletes the work point. Optionally the dependent objects will be deleted. This method will fail in the case where this object was created as a result of a derived part. The HasReferenceComponent property can be used to determine when this is the case. |
| [GetReferenceKey](../WorkPointProxy/WorkPointProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [SetAtCentroid](../WorkPointProxy/WorkPointProxy_SetAtCentroid.md) | Method that redefines a work point to be located at the centroid of the input entities. |
| [SetByCurveAndEntity](../WorkPointProxy/WorkPointProxy_SetByCurveAndEntity.md) | Method that redefines a work point to be at the intersection of the input curve and an entity. |
| [SetByMidPoint](../WorkPointProxy/WorkPointProxy_SetByMidPoint.md) | Method that redefines the work point to be at the midpoint of the input edge. |
| [SetByPoint](../WorkPointProxy/WorkPointProxy_SetByPoint.md) | Method that redefines the work point to be at the input point. |
| [SetBySphereCenterPoint](../WorkPointProxy/WorkPointProxy_SetBySphereCenterPoint.md) | Redefines the work point to be at the center of the Sphere specified by the input face. |
| [SetByThreePlanes](../WorkPointProxy/WorkPointProxy_SetByThreePlanes.md) | Method that redefines the work point to be at the intersection of the three input planes. |
| [SetByTorusCenterPoint](../WorkPointProxy/WorkPointProxy_SetByTorusCenterPoint.md) | Method that redefines the work point to be at the center of the torus specified by the input face. |
| [SetByTwoLines](../WorkPointProxy/WorkPointProxy_SetByTwoLines.md) | Method that redefines the work point to be at the intersection of the two input lines. |
| [SetEndOfPart](../WorkPointProxy/WorkPointProxy_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. The argument defines if the end-of-part marker will be positioned just before or just after the object. If the object is contained within another object and is not in the top level of the browser, the positioning of the marker will be relative to the top-level object the calling object is contained within. An example of this case is a sketch that has not been shared and has been consumed by a feature. Another example is a nested work feature. |
| [SetFixed](../WorkPointProxy/WorkPointProxy_SetFixed.md) | Method that redefines the work point to be at the position specified by the input point. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Adaptive](../WorkPointProxy/WorkPointProxy_Adaptive.md) | Specifies whether the work point is adaptive. |
| [Application](../WorkPointProxy/WorkPointProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../WorkPointProxy/WorkPointProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [Construction](../WorkPointProxy/WorkPointProxy_Construction.md) | Boolean property that returns whether the work point is a construction work point or not. A construction work point is hidden from the user and is not displayed graphically or listed in the browser. Some properties and methods of the WorkPoint object will behave differently for a construction work point. These are Adaptive, Name, and Visible. |
| [Consumed](../WorkPointProxy/WorkPointProxy_Consumed.md) | Gets whether the WorkPoint is consumed or not. |
| [ConsumeInputs](../WorkPointProxy/WorkPointProxy_ConsumeInputs.md) | Gets and sets whether the inputs to this feature should be nested under this feature in the browser. |
| [ContainingOccurrence](../WorkPointProxy/WorkPointProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [Definition](../WorkPointProxy/WorkPointProxy_Definition.md) | Property that returns one of the work point definition objects. Which definition object returned will depend on how the work point is defined. The DefinitionType property can be used to determine the type of definition the Definition property will return. |
| [DefinitionType](../WorkPointProxy/WorkPointProxy_DefinitionType.md) | Property that returns the type of definition that is used to define the work axis. This can be kThreePlanesWorkPoint, kTwoLinesWorkPoint, kCurveAndEntityWorkPoint, kPointWorkPoint, kMidPointWorkPoint, kNonLinearEdgeWorkPoint, kCentroidWorkPoint, kFixedWorkPoint, kTorusCenterPointWorkPoint and kAssemblyWorkPoint. |
| [Dependents](../WorkPointProxy/WorkPointProxy_Dependents.md) | Property that returns the collection of objects that have a direct dependency on the work point. |
| [DrivenBy](../WorkPointProxy/WorkPointProxy_DrivenBy.md) | Property that returns the collection of objects that the work point is dependent on. |
| [Exported](../WorkPointProxy/WorkPointProxy_Exported.md) | Read-write property that gets and sets whether the object is exported. Objects must be marked for export in order for them to be derived. |
| [Grounded](../WorkPointProxy/WorkPointProxy_Grounded.md) | Gets/Sets the Boolean flag that specifies whether this work point is grounded or not. |
| [HasReferenceComponent](../WorkPointProxy/WorkPointProxy_HasReferenceComponent.md) | Property that specifies if the object was created as the result of a derived part. |
| [HealthStatus](../WorkPointProxy/WorkPointProxy_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [IsCoordinateSystemElement](../WorkPointProxy/WorkPointProxy_IsCoordinateSystemElement.md) | Property that returns whether the work point belongs to a coordinate system. If so, edits and delete are not allowed. |
| [IsOwnedByFeature](../WorkPointProxy/WorkPointProxy_IsOwnedByFeature.md) | Property that returns whether this object is owned by a feature. If True, the OwnedBy property returns the owning feature. |
| [IsParentSketch](../WorkPointProxy/WorkPointProxy_IsParentSketch.md) | Property that indicates whether the work point belongs to a 3d sketch. |
| [IsPatternElement](../WorkPointProxy/WorkPointProxy_IsPatternElement.md) | Property that gets whether the work point was created by a pattern. If so, edits and delete are not allowed. |
| [Name](../WorkPointProxy/WorkPointProxy_Name.md) | Specifies the name of the work point. |
| [NativeObject](../WorkPointProxy/WorkPointProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [OwnedBy](../WorkPointProxy/WorkPointProxy_OwnedBy.md) | Read-only property that returns the client feature that owns this object. This property returns Nothing if the IsOwnedByFeature property returns False. |
| [Parent](../WorkPointProxy/WorkPointProxy_Parent.md) | Property returning the parent  object. |
| [ParentSketch](../WorkPointProxy/WorkPointProxy_ParentSketch.md) | Property that returns the parent ComponentDefinition object. |
| [Point](../WorkPointProxy/WorkPointProxy_Point.md) | Property that returns a Point geometry object. The Point object returned provides information about the position of the work point. |
| [ReferenceComponent](../WorkPointProxy/WorkPointProxy_ReferenceComponent.md) | Property that returns the ReferenceComponent that resulted in the creation of this feature. |
| [ReferencedEntity](../WorkPointProxy/WorkPointProxy_ReferencedEntity.md) | Property that returns the referenced WorkPoint in the case where this work point was created using a referenced component. An example of this is when a work point is selected as part of a derived part. The HasReferenceComponent property indicates if this work point is based on a referenced component or not. This property returns Nothing in the case where it is not based on a referenced component. |
| [Shared](../WorkPointProxy/WorkPointProxy_Shared.md) | Gets and sets whether the work point is shared or not. |
| [Type](../WorkPointProxy/WorkPointProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Visible](../WorkPointProxy/WorkPointProxy_Visible.md) | Specifies the visibility of the work point. |

## Version

Introduced in version 5
