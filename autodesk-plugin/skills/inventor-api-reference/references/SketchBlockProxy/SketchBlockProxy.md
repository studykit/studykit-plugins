# SketchBlockProxy Object

Derived from: [SketchBlock](../SketchBlock/SketchBlock.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../SketchBlockProxy/SketchBlockProxy_Delete.md) | Method that deletes the sketch block. |
| [Edit](../SketchBlockProxy/SketchBlockProxy_Edit.md) | Method that activates the sketch block for editing by the user. |
| [ExitEdit](../SketchBlockProxy/SketchBlockProxy_ExitEdit.md) | Method that causes the sketch block to return from the edit mode and into the environment specified by the input argument. If the sketch block is not currently active (i.e. this is not the same block as returned by Application.ActiveEditObject property), then this method does nothing. |
| [Explode](../SketchBlockProxy/SketchBlockProxy_Explode.md) | Method that explodes the contents of the block and deletes the block instance. Note that the contents of the block are retained. |
| [GetCustomLineType](../SketchBlockProxy/SketchBlockProxy_GetCustomLineType.md) | Method that returns information regarding the custom line type in use. The method returns a failure if the return value of the LineType property is not kCustomLineType. |
| [GetObject](../SketchBlockProxy/SketchBlockProxy_GetObject.md) | Method that returns the corresponding object in the sketch block for the given object from it's definition. |
| [GetReferenceKey](../SketchBlockProxy/SketchBlockProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [SetCustomLineType](../SketchBlockProxy/SketchBlockProxy_SetCustomLineType.md) | Method that sets a custom line type to the curve from the specified .lin file. The method automatically changes the value of LineType property to kCustomLineType. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../SketchBlockProxy/SketchBlockProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../SketchBlockProxy/SketchBlockProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ChildBlocks](../SketchBlockProxy/SketchBlockProxy_ChildBlocks.md) | Property that returns an enumerator of SketchBlocks objects found directly under this sketch block. |
| [Color](../SketchBlockProxy/SketchBlockProxy_Color.md) | Gets and sets the color for the sketch block. Setting the property to Nothing restores the sketch block to the default color. |
| [ConstraintStatus](../SketchBlockProxy/SketchBlockProxy_ConstraintStatus.md) | Property that returns the constraint status of the sketch block. Possible return values are kFullyConstrainedConstraintStatus, kOverConstrainedConstraintStatus, kUnderConstrainedConstraintStatus and kUnknownConstraintStatus. |
| [ContainingOccurrence](../SketchBlockProxy/SketchBlockProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [ContainingSketchBlock](../SketchBlockProxy/SketchBlockProxy_ContainingSketchBlock.md) | Property that returns the sketch block that in turn contains this sketch block. This is the same SketchBlock returned as the last item in the SketchBlockPath property. This property \returns Nothing if this sketch block does not belong to another sketch block and lives directly under a sketch. |
| [Definition](../SketchBlockProxy/SketchBlockProxy_Definition.md) | Property that returns the referenced sketch block definition. |
| [Exported](../SketchBlockProxy/SketchBlockProxy_Exported.md) | Read-write property that gets and sets whether the object is exported. Objects must be marked for export in order for them to be derived. |
| [Flexible](../SketchBlockProxy/SketchBlockProxy_Flexible.md) | Gets and sets whether this sketch block is flexible. |
| [HasReferenceComponent](../SketchBlockProxy/SketchBlockProxy_HasReferenceComponent.md) | Property that specifies if the object was created as the result of a derived part. |
| [LineType](../SketchBlockProxy/SketchBlockProxy_LineType.md) | Gets and sets the line type override for the sketch block. |
| [LineWeight](../SketchBlockProxy/SketchBlockProxy_LineWeight.md) | Gets and sets the line weight override for the sketch block. |
| [Name](../SketchBlockProxy/SketchBlockProxy_Name.md) | Gets and sets name of the sketch block. |
| [NativeObject](../SketchBlockProxy/SketchBlockProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [Parent](../SketchBlockProxy/SketchBlockProxy_Parent.md) | Property that returns the parent sketch of the object. |
| [Position](../SketchBlockProxy/SketchBlockProxy_Position.md) | Gets and sets the position of the sketch block. |
| [ReferenceComponent](../SketchBlockProxy/SketchBlockProxy_ReferenceComponent.md) | Property that returns the ReferenceComponent that resulted in the creation of this feature. |
| [ReferencedEntity](../SketchBlockProxy/SketchBlockProxy_ReferencedEntity.md) | Property that returns the referenced sketch block, if there is one. Else, the property returns Nothing. |
| [SketchBlockPath](../SketchBlockProxy/SketchBlockProxy_SketchBlockPath.md) | Property that returns the path of sketch blocks at the leaf of which this sketch block is found. The enumerator returns a count of 0 if the block lives directly under a sketch. The path does not include this sketch block itself. |
| [Transformation](../SketchBlockProxy/SketchBlockProxy_Transformation.md) | Gets and sets the transformation matrix for the sketch block. |
| [Type](../SketchBlockProxy/SketchBlockProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Visible](../SketchBlockProxy/SketchBlockProxy_Visible.md) | Gets and sets whether this sketch block is visible. |

## Version

Introduced in version 2010
