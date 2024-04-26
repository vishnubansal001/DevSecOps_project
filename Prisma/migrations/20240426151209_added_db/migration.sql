-- CreateTable
CREATE TABLE "Product" (
    "identifier" SERIAL NOT NULL,
    "fullName" TEXT NOT NULL,
    "shortName" TEXT NOT NULL,
    "version" TEXT NOT NULL,
    "configuration" TEXT NOT NULL,
    "status" TEXT NOT NULL,
    "centralIntakeRequest" TEXT NOT NULL,

    CONSTRAINT "Product_pkey" PRIMARY KEY ("identifier")
);

-- CreateTable
CREATE TABLE "Component" (
    "identifier" SERIAL NOT NULL,
    "created" INTEGER NOT NULL,
    "fullName" TEXT NOT NULL,
    "shortName" TEXT NOT NULL,
    "version" TEXT NOT NULL,
    "configuration" TEXT NOT NULL,
    "status" TEXT NOT NULL,

    CONSTRAINT "Component_pkey" PRIMARY KEY ("identifier")
);

-- CreateTable
CREATE TABLE "ComponentHistory" (
    "identifier" SERIAL NOT NULL,
    "created" INTEGER NOT NULL,
    "componentId" INTEGER NOT NULL,
    "operatorId" INTEGER NOT NULL,
    "previousVersion" TEXT NOT NULL,
    "previousStatus" TEXT NOT NULL,

    CONSTRAINT "ComponentHistory_pkey" PRIMARY KEY ("identifier")
);

-- CreateTable
CREATE TABLE "Configuration" (
    "identifier" SERIAL NOT NULL,
    "source" TEXT NOT NULL,
    "version" TEXT NOT NULL,

    CONSTRAINT "Configuration_pkey" PRIMARY KEY ("identifier")
);

-- CreateTable
CREATE TABLE "Environment" (
    "identifier" SERIAL NOT NULL,
    "fullName" TEXT NOT NULL,
    "shortName" TEXT NOT NULL,
    "configurationId" INTEGER NOT NULL,

    CONSTRAINT "Environment_pkey" PRIMARY KEY ("identifier")
);

-- CreateTable
CREATE TABLE "Metal" (
    "identifier" SERIAL NOT NULL,
    "fullName" TEXT NOT NULL,
    "shortName" TEXT NOT NULL,
    "configurationId" INTEGER NOT NULL,

    CONSTRAINT "Metal_pkey" PRIMARY KEY ("identifier")
);

-- CreateTable
CREATE TABLE "MetalEnvironment" (
    "identifier" SERIAL NOT NULL,
    "metalId" INTEGER NOT NULL,
    "environmentId" INTEGER NOT NULL,

    CONSTRAINT "MetalEnvironment_pkey" PRIMARY KEY ("identifier")
);

-- CreateTable
CREATE TABLE "Operator" (
    "identifier" SERIAL NOT NULL,
    "name" TEXT NOT NULL,

    CONSTRAINT "Operator_pkey" PRIMARY KEY ("identifier")
);

-- CreateTable
CREATE TABLE "OperatorRole" (
    "identifier" SERIAL NOT NULL,
    "operatorId" INTEGER NOT NULL,
    "roleId" INTEGER NOT NULL,

    CONSTRAINT "OperatorRole_pkey" PRIMARY KEY ("identifier")
);

-- CreateTable
CREATE TABLE "ProductComponent" (
    "identifier" SERIAL NOT NULL,
    "productId" INTEGER NOT NULL,
    "componentId" INTEGER NOT NULL,

    CONSTRAINT "ProductComponent_pkey" PRIMARY KEY ("identifier")
);

-- CreateTable
CREATE TABLE "ProductHistory" (
    "identifier" SERIAL NOT NULL,
    "created" INTEGER NOT NULL,
    "productId" INTEGER NOT NULL,
    "operatorId" INTEGER NOT NULL,
    "previousVersion" TEXT NOT NULL,
    "previousStatus" TEXT NOT NULL,

    CONSTRAINT "ProductHistory_pkey" PRIMARY KEY ("identifier")
);

-- CreateTable
CREATE TABLE "Release" (
    "identifier" SERIAL NOT NULL,
    "status" TEXT NOT NULL,
    "scope" TEXT NOT NULL,
    "effect" INTEGER NOT NULL,
    "metalEnvironmentId" INTEGER NOT NULL,

    CONSTRAINT "Release_pkey" PRIMARY KEY ("identifier")
);

-- CreateTable
CREATE TABLE "Request" (
    "identifier" SERIAL NOT NULL,
    "created" INTEGER NOT NULL,
    "documentation" TEXT NOT NULL,
    "releaseId" INTEGER NOT NULL,
    "status" TEXT NOT NULL,

    CONSTRAINT "Request_pkey" PRIMARY KEY ("identifier")
);

-- CreateTable
CREATE TABLE "ReleaseHistory" (
    "identifier" SERIAL NOT NULL,
    "created" INTEGER NOT NULL,
    "releaseId" INTEGER NOT NULL,
    "operatorId" INTEGER NOT NULL,
    "previousStatus" TEXT NOT NULL,

    CONSTRAINT "ReleaseHistory_pkey" PRIMARY KEY ("identifier")
);

-- CreateTable
CREATE TABLE "Role" (
    "identifier" SERIAL NOT NULL,
    "role" TEXT NOT NULL,

    CONSTRAINT "Role_pkey" PRIMARY KEY ("identifier")
);

-- CreateTable
CREATE TABLE "ApiResponse" (
    "identifier" SERIAL NOT NULL,
    "code" INTEGER NOT NULL,
    "type" TEXT NOT NULL,
    "message" TEXT NOT NULL,

    CONSTRAINT "ApiResponse_pkey" PRIMARY KEY ("identifier")
);

-- CreateIndex
CREATE UNIQUE INDEX "Product_identifier_key" ON "Product"("identifier");

-- CreateIndex
CREATE UNIQUE INDEX "Component_identifier_key" ON "Component"("identifier");

-- CreateIndex
CREATE UNIQUE INDEX "ComponentHistory_identifier_key" ON "ComponentHistory"("identifier");

-- CreateIndex
CREATE UNIQUE INDEX "Configuration_identifier_key" ON "Configuration"("identifier");

-- CreateIndex
CREATE UNIQUE INDEX "Environment_identifier_key" ON "Environment"("identifier");

-- CreateIndex
CREATE UNIQUE INDEX "Metal_identifier_key" ON "Metal"("identifier");

-- CreateIndex
CREATE UNIQUE INDEX "MetalEnvironment_identifier_key" ON "MetalEnvironment"("identifier");

-- CreateIndex
CREATE UNIQUE INDEX "Operator_identifier_key" ON "Operator"("identifier");

-- CreateIndex
CREATE UNIQUE INDEX "OperatorRole_identifier_key" ON "OperatorRole"("identifier");

-- CreateIndex
CREATE UNIQUE INDEX "ProductComponent_identifier_key" ON "ProductComponent"("identifier");

-- CreateIndex
CREATE UNIQUE INDEX "ProductHistory_identifier_key" ON "ProductHistory"("identifier");

-- CreateIndex
CREATE UNIQUE INDEX "Release_identifier_key" ON "Release"("identifier");

-- CreateIndex
CREATE UNIQUE INDEX "Request_identifier_key" ON "Request"("identifier");

-- CreateIndex
CREATE UNIQUE INDEX "ReleaseHistory_identifier_key" ON "ReleaseHistory"("identifier");

-- CreateIndex
CREATE UNIQUE INDEX "Role_identifier_key" ON "Role"("identifier");

-- CreateIndex
CREATE UNIQUE INDEX "ApiResponse_identifier_key" ON "ApiResponse"("identifier");
