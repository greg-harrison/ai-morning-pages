# Stage 1: Building the code
FROM node:20-alpine as builder

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json to /app
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of your Next.js application source code to /app
COPY . .

# Build your Next.js application
RUN npm run build

# Stage 2: Run the built application
FROM node:20-alpine

WORKDIR /app

# Copy the build output to the new working directory
COPY --from=builder /app/next.config.js ./
COPY --from=builder /app/public ./public
# Ensure the .next directory, generated during the build, is copied
COPY --from=builder /app/.next ./.next
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/package.json ./package.json

# Expose the port Next.js runs on
EXPOSE 3000

# Command to run the application
CMD ["npm", "start"]
