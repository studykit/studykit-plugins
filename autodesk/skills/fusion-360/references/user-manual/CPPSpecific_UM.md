## C++ Specific Issues

Fusion has a single API that can be used from several different programming languages. In most cases, the API is used in a very similar way from each of the programming languages with just small language specific syntax changes. However, in some cases there are significant differences in how the API is used because of a particular language. This topic discusses the differences that are unique to C++ and covers the subjects listed below.

* [OS Specific Issues](#OS Specific Issues)
* [Object Declaration](#Object Declaration)
* [Handling Errors](#Handling Errors)
* [Properties](#Properties)
* [Object Types and Casting](#Object Types and Casting)
* [Events](#Events)
* [Header Files](#Header Files)
* [Iteration](#Iteration)
* [Object Equality](#Object Equality)
* [Utility Functions](#Utility Functions)
* [Debugging a Windows Script or Add-In](#Debugging a Windows Script or Add-In)
* [Debugging a Mac Script or Add-In](#Debugging a Mac Script or Add-In)

### OS Specific Issues

When creating a new C++ script or add-in using the “Scripts and Add-Ins” command a single cpp is created and both Visual Studio (.vcxproj) and Xcode (.xcodeproj) projects are created that use the single cpp. In most cases the same code can be used on both Windows and Mac unless you’ve chosen to use an external library that is OS specific. Even though it’s usually possible that the same source code can be used for both Mac and Windows, the binary that’s used by Fusion is OS specific. This means you need to use Windows and Visual Studio to compile your script or add-in for Windows and OS X and Xcode to compile it for Mac.

Most of the discussion below is about the code of your script or add-in and is platform agnostic so it applies to both Mac and Windows. The last topic describes debugging your script or add-in which is OS specific.

### Object Declaration

Variables declarations and function arguments that use a Fusion defined type should always use the Fusion defined Ptr template to create a smart pointer. A smart pointer will automatically handle adding and removing references, deleting the reference when it’s no longer needed (i.e. when the variable goes out of scope or is explicitly set to nullptr), and casting.

```
Ptr<SketchLine> line1;

bool doAnimation(Ptr<SketchCurve> pathCurve, Ptr<Vector3D> upDirection)
{
}
```

### Handling Errors

In the C++ implementation of the Fusion API, all errors are reported through error codes. There are not asserts fired so a try catch statement will not work. In most cases this means one of two things. First, if a function is expected to return an object, it will either return the expected object or some other documented result (usually null) indicating the function failed. This is demonstrated below.

```
Ptr<SketchLine> ln = lines->addByTwoPoints(p1, p2);
if (!ln)
    return false;
```

If the function failed you can obtain additional information about the failure by using the getLastError method of the Application object. This is demonstrated below:

```
Ptr<SketchLine> ln;
ln = lines->addByTwoPoints(p1, p2);
If (!ln)
{
    // get error message
    std::string errorMessage;
    int errorCode = app->getLastError(&errorMessage);
    if (GenericErrors::Ok != errorCode)
        ui->messageBox(errorMessage);
    return false;
}
```

The second error reporting method is for functions that return a Boolean indicating success or failure, as demonstrated below. Again, you can use the getLastError method to get more information about the error.

```
bool isOK = sk->isComputeDeferred(false);
if (!isOK)
    return false;
```

### Properties

C++ doesn’t support properties in the way they are defined in the API and as they are used by Python. The Python sample below illustrates using the read-write name property of the Component object to get the existing name of a component and then set it.

```
// Python
if comp.name == "Test":
    comp.name = "New Test"
```